from random import randint
import requests
from odoo.http import request
from odoo import api, fields, models

class Comunicados(models.Model):
    _name = 'oe.school.comunicados'
    
    name = fields.Char(string='name', required=True)
    descripcion = fields.Text(string='descripcion')
    
     
    @api.model
    def create(self, vals):
        new_record = super(Comunicados, self).create(vals)
        print("data de impresion")
        print(vals)
        self.enviarNotificacionComunicado(vals)
        return new_record
    
    def send_notification(self,device_token, title, body):
        print("Clave kkkkkkkksd sdd  ==========",device_token)
        server_key = 'AAAAM-ejTlM:APA91bEqdQRAjd_2_qXK23M9c7CbbDf7SVpjas789C9xMQXtEkUNSHeT4Gj9t3nTOG_Tk6JK9C4qDD1n1r0oZeRtI9otcoi-OhPJDsw93LypxhQpHRvi9ZG9eS_WmT_fHagLHSSZubtF'
        url = 'https://fcm.googleapis.com/fcm/send'
        headers = {
            'Authorization': 'key=' + server_key,
            'Content-Type': 'application/json',
        }
        data = {
            'to': device_token,
            'notification': {
                'title': title,
                'body': body,
            },
        }
        response = requests.post(url, headers=headers, json=data)
        return response.status_code


    def enviarNotificacionComunicado(seft,comunicado):
        print("este es el comunicado " ,comunicado)
        
        name = comunicado.get('name')
        descripcion = comunicado.get('descripcion')
        
        Padres = request.env['oe.school.padre'].sudo().search([])
        
        for padre in Padres:
            mensaje = f"comunicado:  {name}  contexto: {descripcion}"
            print("este es el padre y su key " ,padre.keynotificaciones)
            seft.send_notification(padre.keynotificaciones, 'Nuevos Comunicados', mensaje)
        return