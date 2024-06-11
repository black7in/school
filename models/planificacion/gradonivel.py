from odoo  import models, fields, api

class Grado(models.Model):
    _name = 'school.grado'
    _description = 'Grado académico'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Char(string='Descripción')
    # Cupo de estudiantes
    cupo = fields.Integer(string='Cupo', required=True)
    nivel_id = fields.Many2one('school.nivel', string='Nivel', required=True)
    # Relacion con Asignacion
    asignacion_ids = fields.One2many('school.asignacion', 'grado_id', string='Asignaciones')
    
    
    # Datos computados
    materia_ids = fields.Many2many('school.materia', compute='_compute_materia_ids', string='Materias')
    profesor_ids = fields.Many2many('school.profesor', compute='_compute_profesor_ids', string='Profesores')
    horario_ids = fields.Many2many('school.horario', compute='_compute_horario_ids', string='Horarios')


    @api.depends('name', 'nivel_id')
    def _compute_display_name(self):
        for record in self:
            record.display_name = '%s de %s' % (record.name, record.nivel_id.name if record.nivel_id else '')
            
    @api.depends('asignacion_ids.materia_id')
    def _compute_materia_ids(self):
        for record in self:
            record.materia_ids = record.asignacion_ids.mapped('materia_id')
            
    @api.depends('asignacion_ids.profesor_id')
    def _compute_profesor_ids(self):
        for record in self:
            record.profesor_ids = record.asignacion_ids.mapped('profesor_id')
            
    @api.depends('asignacion_ids.horario_id')
    def _compute_horario_ids(self):
        for record in self:
            record.horario_ids = record.asignacion_ids.mapped('horario_id')

class Nivel(models.Model):
    _name = 'school.nivel'
    _description = 'Nivel académico'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    grado_ids = fields.One2many('school.grado', 'nivel_id', string='Grados académicos')
