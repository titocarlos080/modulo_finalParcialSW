from random import randint
import requests
from odoo.http import request

from odoo import api, fields, models



import logging  # Asegúrate de importar el módulo logging
# Configurar el logger
_logger = logging.getLogger(__name__)

class notas(models.Model):   # hereda de models.models
    _name = 'oe.school.notas'
    codigo = fields.Char(string='codigo', required=True ,size=10)
    name = fields.Char(string='nombre_estudiante', required=True)
    descripcion = fields.Text(string='descripcion')
    gestion = fields.Integer(string='gestion', required=True)
    materia_id = fields.Many2one('oe.school.materia', string='materia_id', required=True)
    student_id = fields.Many2one('res.partner', string='Student', required=True, ondelete='cascade', index=True, copy=False)
    nota = fields.Float(string='Nota', digits=(3, 2), required=True, help="Inserte la nota (máximo 100)")
    
    
    @api.model
    def create(self, vals):
        new_record = super(notas, self).create(vals)
        print("data de impresion")
        print(vals)
        self.enviarNotificacion(vals) 
        return new_record
    
    def enviarNotificacion(self,notas):
        print("ESTAS SON LAS NOTAS QUE SE AGREGARON" ,notas)
        
        student_id = notas.get('student_id')
        print("ESte es el id " ,student_id)
        keyPadre = self.obtenerKeyPadre(notas.get('student_id'))
        
        
        if keyPadre:
            codigo = notas.get('codigo')
            name = notas.get('name')
            descripcion = notas.get('descripcion')
            student_id = notas.get('student_id')
            materia_id = notas.get('materia_id')
            gestion = notas.get('gestion')
            nota = notas.get('nota')
            Materia =  request.env['oe.school.materia'].sudo().search([('id', '=',materia_id)], limit=1)
            mensaje = f"Se subieron las notas del estudiante {name} para la materia {Materia.name}. Nota: {nota}"
            self.send_notification(keyPadre, 'Actualización de Notas', mensaje)
            return
    def obtenerKeyPadre(self,student_id):
         # Lógica para obtener la key de notificación del padre según el ID del estudiante
         
        print("ESte es el id del estudiante  " ,student_id)
         
        #obtener el id padre 
        
        Estudiante =  request.env['res.partner'].sudo().search([('id', '=', student_id)], limit=1)
        
        padreid= Estudiante.padre_id.id
        
        print("ESte es el id  padre   " ,padreid)
        
        padre =  request.env['oe.school.padre'].sudo().search([('id', '=',padreid)], limit=1)
        
        print("ESte es el padre ==   " ,padre)
        print("ESte es el KEY del  padre ==   " ,padre.keynotificaciones)
        
        return padre.keynotificaciones if padre else None

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


    def enviarNotificacionComunicado(self,comunicado):
        print("este es el comunicado " ,comunicado)
        
        name = comunicado.get('name')
        descripcion = comunicado.get('descripcion')
        
        Padres = request.env['oe.school.padre'].sudo().search([])
        
        for padre in Padres:
            mensaje = f"comunicado:  {name}  contexto: {descripcion}"
            print("este es el padre y su key " ,padre.keynotificaciones)
            self.send_notification(padre.keynotificaciones, 'Nuevos Comunicados', mensaje)
        return   