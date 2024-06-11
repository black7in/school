from odoo import models, fields, api

class Inscripcion(models.Model):
    _name = 'school.inscripcion'
    _description = 'Inscripción'
    
    fecha_inscripcion = fields.Date(string='Fecha de inscripción', required=True)
    #active = fields.Boolean(string='Activo', default=True)
    
    # relacion con periodo
    periodo_id = fields.Many2one('school.periodo', string='Periodo', required=True)
    
    # relacion con muchos alumnos
    alumno_id = fields.Many2one('school.alumno', string='Alumno', required=True)
    nivel_id = fields.Many2one('school.nivel', string='Nivel', required=True)
    grado_id = fields.Many2one('school.grado', string='Grado', required=True)