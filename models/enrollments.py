from odoo import api, fields, models

class SchoolEnrollment(models.Model):
    _name = 'school.enrollment'
    _description = 'School Enrollment'
 
    date = fields.Date(string='Enrollment Date', required=True)
 