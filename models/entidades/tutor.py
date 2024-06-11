from odoo import models, fields, api

class Tutor(models.Model):
    _name = 'school.tutor'
    _description = 'Tutor'

    name = fields.Char( string="Nombre", required=True, help="Nombre del tutor")
    lastname = fields.Char( string="Apellido", required=True, help="Apellido del tutor")
    # ci debe ser único
    ci = fields.Char( string="Carnet de Identidad", required=True, help="Carnet de Identidad del tutor", size=10, unique=True)
    # dirección del tutor
    address = fields.Char( string="Dirección", help="Dirección del tutor")
    # teléfono del tutor
    phone = fields.Char( string="Teléfono", help="Teléfono del tutor")
    # correo del tutor
    email = fields.Char( string="Correo Electrónico", help="Correo Electrónico del tutor")
    # relacion con alumnos
    alumno_ids = fields.Many2many(
        'school.alumno',
        string="Alumnos"
        )