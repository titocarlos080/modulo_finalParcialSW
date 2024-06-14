from random import randint
from odoo import api, fields, models


class Nivel(models.Model):
    _name = 'oe.school.nivel'
    
    name = fields.Char(string='nombre', required=True)
    descripcion = fields.Text(string='descripcion')
  
    ciclo = fields.Selection([('primaria', 'primaria'),
                                ('secundaria', 'secundaria'),
                                ('noche', 'noche')], string='ciclo', default="primaria", required=True)



class materia(models.Model):   # hereda de models.models
    _name = 'oe.school.materia'
    codigo = fields.Char(string='codigo', required=True ,size=10)
    name = fields.Char(string='nombre', required=True)
    
    def _default_color(self):
        return randint(1, 11)

    
    creditos = fields.Integer(string='creditos')
    # Relación muchos a uno con el modelo oe.school.nivel
    
    # un nivel esta en muchas materias - la llave de nivel se va a materias
    nivel_id = fields.Many2one('oe.school.nivel', string='Nivel')
    

