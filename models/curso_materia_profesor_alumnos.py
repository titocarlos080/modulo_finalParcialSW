
from odoo import api, fields, models

class cursomateriaprofesoralumnos(models.Model):
    _name = 'oe.school.cursomateriaprofesoralumnos'
    
    
    DIAS_SEMANA = [
         ('lunes-miercoles-viernes', 'Lunes-Miercoles-Viernes'),
        ('martes-jueves', 'Martes-Jueves'),
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]
    
    name = fields.Char(string="curso_materia_gestion",required=True,help="Debe colocar un formato curso-materia-gestion")
    
    gestion = fields.Integer(string='gestion', required=True)
    
    descripcion = fields.Text(string='descripcion')
    # un nivel esta en muchas materias - la llave de nivel se va a materias
    curso_id = fields.Many2one('oe.school.course', string='curso_id', required=True)
    materia_id = fields.Many2one('oe.school.materia', string='materia_id', required=True)
    teacher_id = fields.Many2one('hr.employee', string='teacher_id', required=True, ondelete='cascade', index=True, copy=False)

    alumno_ids = fields.Many2many('res.partner', string='alumno_ids', required=True, ondelete='cascade', index=True, copy=False)
    
    hora_inicio = fields.Float(string='Hora de Inicio', required=True, help="Hora de inicio en formato 24h, por ejemplo, 8.5 para las 08:30")
    hora_fin = fields.Float(string='Hora de Fin', required=True, help="Hora de fin en formato 24h, por ejemplo, 15.5 para las 15:30")
    
    dia_semana = fields.Selection(DIAS_SEMANA, string='Días de la Semana', multiple=True)
