from odoo import models, fields, api

# Case Materia con relación a Grado de muchos a muchos
class Materia(models.Model):
    _name = 'school.materia'
    _description = 'Materia'

    name = fields.Char(string='Nombre', required=True)
    sigla = fields.Char(string='Sigla', required=True)
    description = fields.Text(string='Descripción')
    
    # Relacion con Asignacion
    asignacion_ids = fields.One2many('school.asignacion', 'materia_id', string='Asignaciones')
    profesor_id = fields.Many2one('school.profesor', compute='_compute_profesor_id', string='Profesor')


    @api.depends('name', 'sigla')
    def _compute_display_name(self):
        for record in self:
            record.display_name = '%s %s' % (record.sigla, record.name)
    
    def _compute_profesor_id(self):
        for record in self:
            asignacion = self.env['school.asignacion'].search([('materia_id', '=', record.id)], limit=1)
            record.profesor_id = asignacion.profesor_id