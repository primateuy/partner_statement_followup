��            )   �      �  �  �  &   9  -   `     �     �     �     �     �     �  
   �     �     �     �     �               #     +     2  )   F     p  f   x     �     �     �               (     .  }  O	  /   �  )   �     '     3     B     _     g     m  
   {     �     �     �     �     �     �     �     �       8   !  	   Z  �   d     �     �               %     6        	                                                                                                                              
    <?xml version="1.0"?>
<div style="margin: 0px; padding: 0px;">
                    <p style="margin: 0px; padding: 0px; font-size: 13px;">
                        Dear ${object.name}<br/><br/>
                        Please find enclosed your statement of account with the outstanding amounts. We remind you of the importance of
                        regularize your debt as soon as possible.
                        If you have already paid, please ignore this message.
                        If not, please contact us to discuss possible solutions.
                        <br/><br/>
                        Thank you for your prompt attention to this matter.
                        <br/><br/>
                        Sincerely,<br/>
                        % if user and user.signature:
                        ${user.signature | safe}
                        % endif
                    </p>
                </div>
             <strong> Next execution date </strong> Account statement of ${object.name or 'n/a' } Auto CC's Cron Run Followups Customer Days Execute Every ExtPartner Followup Followup Method Hours Interval Number Interval Unit Last Execution Date Minutes Months Next Execution Date Next planned execution date for this job. Pending Previous time the cron ran successfully, provided to the job through the context on the `lastcall` key Related Cron Repeat every x. Report to send Run Row Statement of Account Weeks Project-Id-Version: Odoo Server 13.0-20210523
Report-Msgid-Bugs-To: 
PO-Revision-Date: 2023-11-06 22:57-0300
Last-Translator: 
Language-Team: 
MIME-Version: 1.0
Content-Type: text/plain; charset=UTF-8
Content-Transfer-Encoding: 8bit
Plural-Forms: 
Language: es_UY
X-Generator: Poedit 2.3
 <?xml version="1.0"?>
<div style="margin: 0px; padding: 0px;">
                    <p style="margin: 0px; padding: 0px; font-size: 13px;">
                        Estimado ${object.name}<br/><br/>
                        Adjunto tu estado de cuenta con los montos pendientes.
                        Te recordamos la importancia de regularizar tu deuda a la brevedad posible.
                        Si ya has realizado el pago, ignora este mensaje. En caso contrario, por favor, contáctanos para discutir posibles soluciones.
                        <br/><br/>
                        Gracias por tu pronta atención a este asunto.
                        <br/><br/>
                        Atentamente,<br/>
                        % if user and user.signature:
                        ${user.signature | safe}
                        % endif
                    </p>
                </div> <strong> Próxima fecha de ejecución </strong> Estado de Cuenta ${object.name or 'n/a' } Automático Poner en copia Ejecutar cron de Seguimiento Cliente Días Ejecutar cada ExtPartner Seguimientos Método de seguimiento Horas Número de intervalo Unidad de intervalo Última fecha de ejecución Minutos	 Meses Próxima fecha de ejecución Próxima fecha de ejecución prevista para este trabajo. Pendiente Hora anterior en la que el cron se ejecutó correctamente, proporcionada al trabajo a través del contexto en la tecla `lastcall cron relacionado Repetir cada x Reporte a enviar Ejecutar ahora Estado de cuenta Semanas 