# -*- coding: utf-8 -*-
{
    "name": "Partner Statement Followup",
    "version": "13.0.1.3.0.06.11.2023.23.00",
    "price": 28.00,
    "currency": "USD",
    "category": "Accounting",
    "summary": "Extension module for Partner Statement",
    "author": "Proyecta, Primate",
    "website": "https://primate.uy",
    "license": "AGPL-3",
    "depends": ["account"],
    "data": [
        'data/ir_cron_data.xml',
        'data/mail_template.xml',
        'views/res_partner_view.xml',
    ],
    "installable": True,
    "application": False,
}
