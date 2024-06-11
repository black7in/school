from odoo import models, fields, api

class Bloque(models.Model):
    _name = 'school.bloque'
    _description = 'Bloque, Edificio o Piso'

    name = fields.Char(string='Nombre', required=True)
    description = fields.Text(string='Descripción')
    
    # Relacion uno a muchos con Aula
    aula_ids = fields.One2many('school.aula', 'bloque_id', string='Aulas')