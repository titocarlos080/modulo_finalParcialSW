from random import randint

from requests import request
from odoo.addons.modulo_escolar.controllers.notificacion_controller import NotificacionController # type: ignore
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
        NotificacionController.enviarNotificacion(vals)
        return new_record
       