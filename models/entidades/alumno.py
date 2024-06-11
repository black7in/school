from odoo import models, fields, api
from collections import defaultdict

class Alumno(models.Model):
    _name = 'school.alumno'
    _description = 'Alumno'

    name = fields.Char( string="Nombre", required=True, help="Nombre del alumno")
    lastname = fields.Char( string="Apellido", required=True, help="Apellido del alumno")
    # ci debe ser único
    ci = fields.Char( string="Carnet de Identidad", required=True, help="Carnet de Identidad del alumno", size=10, unique=True)
    # fecha de nacimiento
    birthdate = fields.Date( string="Fecha de Nacimiento", required=True, help="Fecha de Nacimiento del alumno")
    # sexo Masulino o Femenino
    sexo = fields.Selection([('M', 'Masculino'), ('F', 'Femenino')], string="Sexo", required=True, help="Sexo del alumno")
    # dirección del alumno
    address = fields.Char( string="Dirección", help="Dirección del alumno")
    # teléfono del alumno
    phone = fields.Char( string="Teléfono", help="Teléfono del alumno")
    # correo del alumno
    email = fields.Char( string="Correo Electrónico", help="Correo Electrónico del alumno")
    # foto del alumno
    photo = fields.Binary( string="Foto", help="Foto del alumno")
    # relación con tutor
    tutor_ids = fields.Many2many('school.tutor', string="Tutores")
    #relacion con muchas inscripciones
    inscripcion_ids = fields.One2many('school.inscripcion', 'alumno_id', string="Inscripciones")
    
    # Datos computados
    last_periodo_id = fields.Many2one('school.periodo', compute='_compute_last_periodo', string="Gestion")
    last_grade_id = fields.Many2one('school.grado', compute='_compute_last_grade', string="Grado")
    last_horario_id = fields.Many2one('school.horario', compute='_compute_last_horario', string="Último Horario")
    last_asignaciones_ids = fields.One2many('school.asignacion', compute='_compute_last_asignaciones', string="Últimas Asignaciones")
    last_asignaciones_grouped = fields.Text(compute='_compute_last_asignaciones_grouped', string="Últimas Asignaciones Agrupadas")

    @api.depends('name', 'lastname')
    def _compute_display_name(self):
        for record in self:
            record.display_name = '%s %s' % (record.name, record.lastname)
            
    @api.depends('inscripcion_ids.periodo_id.date_start', 'inscripcion_ids.grado_id')
    def _compute_last_grade(self):
        for record in self:
            last_inscription = record.inscripcion_ids.filtered(lambda r: r.periodo_id).sorted(key=lambda r: r.periodo_id.date_start, reverse=True)[:1]
            record.last_grade_id = last_inscription.grado_id if last_inscription else None

    @api.depends('inscripcion_ids.periodo_id.date_start')
    def _compute_last_periodo(self):
        for record in self:
            last_inscription = record.inscripcion_ids.filtered(lambda r: r.periodo_id).sorted(key=lambda r: r.periodo_id.date_start, reverse=True)[:1]
            record.last_periodo_id = last_inscription.periodo_id if last_inscription else None
            
    @api.depends('inscripcion_ids.periodo_id.date_start', 'inscripcion_ids.grado_id')
    def _compute_last_horario(self):
        for record in self:
            last_inscription = record.inscripcion_ids.filtered(lambda r: r.periodo_id and r.grado_id).sorted(key=lambda r: r.periodo_id.date_start, reverse=True)[:1]
            if last_inscription:
                asignacion = self.env['school.asignacion'].search([('grado_id', '=', last_inscription.grado_id.id)], limit=1)
                record.last_horario_id = asignacion.horario_id if asignacion else None
            else:
                record.last_horario_id = None
                
    @api.depends('last_grade_id')
    def _compute_last_asignaciones(self):
        for record in self:
            if record.last_grade_id:
                record.last_asignaciones_ids = self.env['school.asignacion'].search([('grado_id', '=', record.last_grade_id.id)])
            else:
                record.last_asignaciones_ids = self.env['school.asignacion']
                
    @api.depends('last_grade_id')
    def _compute_last_asignaciones_grouped(self):
        for record in self:
            if record.last_grade_id:
                asignaciones = self.env['school.asignacion'].search([('grado_id', '=', record.last_grade_id.id)])
                grouped_asignaciones = defaultdict(list)
                for asignacion in asignaciones:
                    grouped_asignaciones[asignacion.materia_id.name].append({
                        'aula': asignacion.aula_id.name,
                        'dia': asignacion.horario_id.dia_simbolo,
                        'hora_inicio': asignacion.horario_id.hora_inicio,
                        'hora_fin': asignacion.horario_id.hora_fin,
                    })
                record.last_asignaciones_grouped = str(dict(grouped_asignaciones))
            else:
                record.last_asignaciones_grouped = ''