# -*- coding: utf-8 -*-
import base64
from odoo import models, fields, api
from dateutil.relativedelta import relativedelta


class Partner(models.Model):
    _inherit = 'res.partner'

    cron_id = fields.Many2one(comodel_name='ir.cron', compute='get_cron', string='Related Cron')
    customer = fields.Boolean(default=True)
    followup_method = fields.Selection([('manual', 'Manual'), ('auto', 'Auto')], string="Followup Method",
                                       default="manual")
    followup_report = fields.Selection(
        [('activity.statement.wizard', 'Statement of Account'), ('outstanding.statement.wizard', 'Pending')],
        string="Report to send", default="activity.statement.wizard")
    interval_number = fields.Integer(default=1, help="Repeat every x.")
    interval_type = fields.Selection([('minutes', 'Minutes'),
                                      ('hours', 'Hours'),
                                      ('days', 'Days'),
                                      ('weeks', 'Weeks'),
                                      ('months', 'Months')], string='Interval Unit', default='months')
    nextcall = fields.Datetime(string='Next Execution Date', required=True, default=fields.Datetime.now,
                               help="Next planned execution date for this job.")
    lastcall = fields.Datetime(string='Last Execution Date',
                               help="Previous time the cron ran successfully, provided to the job through the context on the `lastcall` key")
    nofitier_ids = fields.Many2many(comodel_name='res.partner', column2='res_id', column1='partner_id',
                                    relation='partner_notify_rel', string="CC's")

    def get_cron(self):
        for rec in self:
            cron = self.env.ref('partner_statement_followup.cron_run_followups')
            rec.cron_id = cron.id

    def get_email_cc(self):
        users_to_send = ''
        users_to_nofity = self.nofitier_ids.filtered(lambda x: x.email)
        if len(users_to_nofity) > 1:
            lastindex = len(users_to_nofity)
            _iter = 0
            for user in users_to_nofity:
                _iter += 1
                if lastindex != _iter:
                    users_to_send += user.email + ';'
                if lastindex == _iter:
                    users_to_send += user.email
        else:
            users_to_send = users_to_nofity.email

        return users_to_send

    def run_followup(self):
        ctx = self.env.context.copy()
        if not self.followup_report:
            return
        activity_wizard_obj = self.env[self.followup_report]
        activity_wizard = activity_wizard_obj.with_context(active_ids=self.ids, lang=self.lang).create({})
        res = activity_wizard.button_export_pdf()
        report_name = res['report_name']
        report = self.env['ir.actions.report']._get_report_from_name(report_name)
        content, extension = report.render_qweb_pdf(self.ids)
        b64_pdf = base64.b64encode(content)
        attachment_name = f'{res["name"]}{self.name}.{extension}'
        attachment_obj = self.env['ir.attachment']
        attachment = attachment_obj.create({
            'type': 'binary',
            'datas': b64_pdf,
            'name': attachment_name,
            'store_fname': attachment_name,
            'res_model': self._name,
            'res_id': self.id,
            'mimetype': 'application/pdf'
        })
        template = self.env.ref('partner_statement_followup.mail_template_followup').get_email_template(self.id)
        template_ctx = template._context.copy()
        template_ctx['email_from'] = self.env.company.email
        body_html = self.env['mail.template'].with_context(template_ctx)._render_template(template.body_html, self._name, self.id)
        mail_id = template.send_mail(self.id)
        mail = self.env['mail.mail'].browse(mail_id)
        mail.attachment_ids += attachment
        self.message_notify(
            body=body_html,
            partner_ids=[self.id],
            subtype='mail.mt_comment',
            email_layout_xmlid='mail.mail_notification_light',
        )

        mail.send()
        if ctx.get('manually_ran', False):
            periods = {'minutes': 'minutes', 'hours': 'hours', 'days': 'days', 'weeks': 'weeks', 'months': 'months'}
            self.lastcall = fields.Datetime.now()
            new_date = self.lastcall + relativedelta(**{periods[self.interval_type]: self.interval_number})
            self.nextcall = new_date

    def cron_run_followups(self):
        partners = self.search([('followup_method', '=', 'auto'), ('nextcall', '<=', fields.Datetime.now())])
        for partner in partners:
            if not partner.cron_id:
                partner.get_cron()
            cron = partner.cron_id
            if partner.nextcall > partner.cron_id.nextcall:
                continue

            partner.run_followup()
            partner.lastcall = self.env.context.get('lastcall')
            partner.nextcall = cron.nextcall
