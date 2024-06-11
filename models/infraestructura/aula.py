from odoo import models, fields, api

class Aula(models.Model):
    _name = 'school.aula'
    _description = 'Aula'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    capacidad = fields.Integer(string='Capacidad')    
    
    # Relacion uno a muchos con Bloque
    bloque_id = fields.Many2one('school.bloque', string='Bloque')
    
    # Relacion con Asignacion
    asignacion_ids = fields.One2many('school.asignacion', 'aula_id', string='Asignaciones')
    
    