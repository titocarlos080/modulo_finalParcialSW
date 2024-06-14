
from odoo import api, fields, models


class inscripcion(models.Model):
    _name = 'oe.school.inscripcion'
    
    gestion = fields.Integer(string='gestion', required=True)
    
    descripcion = fields.Text(string='descripcion')
    
    # un nivel esta en muchas materias - la llave de nivel se va a materias
    nivel_id = fields.Many2one('oe.school.nivel', string='Nivel')
    
    student_id = fields.Many2one('res.partner', string='Student', required=True, ondelete='cascade', index=True, copy=False)
    curso_id = fields.Many2one('oe.school.course', string='Curso', required=True)
    
    
