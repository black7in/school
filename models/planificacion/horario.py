from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Horario(models.Model):
    _name = 'school.horario'
    _description = 'Horario'    
    
    hora_inicio = fields.Float(string='Hora de inicio', required=True)
    hora_fin = fields.Float(string='Hora de fin', required=True)
    dia = fields.Selection([
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
    ], string='Día', required=True)
    dia_simbolo = fields.Char(string='Símbolo del día')
    # Relacion con Asignacion
    asignacion_ids = fields.One2many('school.asignacion', 'horario_id', string='Asignaciones')

    @api.onchange('dia')
    def _onchange_dia(self):
        simbolos = {
            'lunes': 'L',
            'martes': 'M',
            'miercoles': 'Mi',
            'jueves': 'J',
            'viernes': 'V',
            'sabado': 'S',
        }
        self.dia_simbolo = simbolos.get(self.dia, '')
        
    @api.depends('dia_simbolo', 'hora_inicio', 'hora_fin')
    def _compute_display_name(self):
        for record in self:
            hora_inicio = '%02d:%02d' % (int(record.hora_inicio), int((record.hora_inicio % 1) * 60))
            hora_fin = '%02d:%02d' % (int(record.hora_fin), int((record.hora_fin % 1) * 60))
            record.display_name = '%s - Horas: %s - %s' % (record.dia_simbolo, hora_inicio, hora_fin)
    
    
    
# Asignacion es un modelo para relacionar grado, materia, horario, aula
class Asignacion(models.Model):
    _name = 'school.asignacion'
    _description = 'Asignación'
    _sql_constraints = [
        ('unique_grado_horario',
         'UNIQUE(grado_id, horario_id)',
         'Choque de horario, ya tiene una materia asignada! elija otro horario'),
    ]
    
    #Relacion con Grado
    grado_id = fields.Many2one('school.grado', string='Grado', required=True)
    # Relacion con Materias
    materia_id = fields.Many2one('school.materia', string='Materia', required=True)
    # Relacion con Profesor
    profesor_id = fields.Many2one('school.profesor', string='Profesor', required=True)
    # Relacion con Aula
    aula_id = fields.Many2one('school.aula', string='Aula', required=True)
    # Relacion con Horario
    horario_id = fields.Many2one('school.horario', string='Horario', required=True)
     # Add a reverse relation to 'Grado'
    grado_id = fields.Many2one('school.grado', string='Grado', required=True, inverse_name='asignacion_ids')

    @api.onchange('materia_id')
    def _onchange_materia_id(self):
        return {'domain': {'profesor_id': [('materia_ids', 'in', self.materia_id.id)]}}
    
    
    