from random import randint
from odoo import api, fields, models
from odoo.addons.de_school.controllers.notificacion_controller import NotificacionController # type: ignore

class Comunicados(models.Model):
    _name = 'oe.school.comunicados'
    
    name = fields.Char(string='name', required=True)
    descripcion = fields.Text(string='descripcion')
    
     
    @api.model
    def create(self, vals):
        new_record = super(Comunicados, self).create(vals)
        print("data de impresion")
        print(vals)
        NotificacionController.enviarNotificacionComunicado(vals)
        return new_record