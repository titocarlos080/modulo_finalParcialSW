from random import randint
from odoo import api, fields, models



class Pago(models.Model):
    _name = 'oe.school.pagos'
     
    monto = fields.Float(string='Monto', required=True)
    descripcion = fields.Text(string='Descripción')
    inscripcion_id = fields.Many2one('oe.school.inscripcion', string='Inscripción')
