from odoo import models, fields, api
from datetime import date

class Periodo(models.Model):
    _name = 'school.periodo'
    _description = 'Periodo académico'
    _sql_constraints = [
        ('date_check', 'CHECK(date_start < date_end)', 'La fecha de inicio debe ser anterior a la fecha de fin'),
        ('date_overlap', 'EXCLUDE USING gist (daterange(date_start, date_end, "both") WITH &&)',
         'No puede haber dos periodos que se superpongan'),
    ]

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    date_start = fields.Date(string='Fecha de inicio', required=True)
    date_end = fields.Date(string='Fecha de fin', required=True)
    
    # Relacion con inscripciones
    inscripcion_ids = fields.One2many('school.inscripcion', 'periodo_id', string='Inscripciones')

    @api.model
    def get_current_period(self):
        today = date.today()
        current_period = self.search([('date_start', '<=', today), ('date_end', '>=', today)], limit=1)
        return current_period