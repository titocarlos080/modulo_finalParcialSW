from random import randint
from odoo import api, fields, models

class Pago(models.Model):
    _name = 'oe.school.pagos'
    
    monto = fields.Float(string='Monto', required=True)
    descripcion = fields.Text(string='Descripción')
    inscripcion_id = fields.Many2one('oe.school.inscripcion', string='Inscripción')

    @api.model
    def create(self, vals):
        # Aquí puedes agregar lógica adicional al crear un registro
        record = super(Pago, self).create(vals)
        return record

    def write(self, vals):
        # Aquí puedes agregar lógica adicional al escribir un registro
        res = super(Pago, self).write(vals)
        return res

    def unlink(self):
        # Aquí puedes agregar lógica adicional al eliminar un registro
        res = super(Pago, self).unlink()
        return res
