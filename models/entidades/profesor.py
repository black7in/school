from odoo import models, fields, api, exceptions

class Profesor(models.Model):
    _name = 'school.profesor'
    _description = 'Profesor'

    name = fields.Char( string="Nombre", required=True, help="Nombre del alumno")
    lastname = fields.Char( string="Apellido", required=True, help="Apellido del alumno")
    # ci debe ser único
    ci = fields.Char( string="Carnet de Identidad", required=True, help="Carnet de Identidad del alumno", size=10, unique=True)
    # dirección del alumno
    address = fields.Char( string="Dirección", help="Dirección del alumno")
    # teléfono del alumno
    phone = fields.Char( string="Teléfono", help="Teléfono del alumno")
    # correo del alumno
    email = fields.Char( string="Correo Electrónico", help="Correo Electrónico del alumno", required=True, unique=True)
    # foto del alumno
    photo = fields.Binary( string="Foto", help="Foto del alumno")
    
    user_id = fields.Many2one('res.users', string='Usuario')
    # Relacion Asignacion
    asignacion_ids = fields.One2many('school.asignacion', 'profesor_id', string='Asignaciones')
    
    @api.model
    def create(self, vals):
        # Crear un nuevo usuario solo si no se asignó uno al crear el profesor
        if 'user_id' not in vals:
            user = self.env['res.users'].create({
                'login': vals.get('email'),
                'password': vals.get('ci'),  # Establecer una contraseña predeterminada
                'name': vals.get('name') + " " + vals.get('lastname'),
                'email': vals.get('email'),
            })
            # Asociar el nuevo usuario con el nuevo profesor
            vals['user_id'] = user.id
        return super(Profesor, self).create(vals)
    
    @api.depends('name', 'lastname')
    def _compute_display_name(self):
        for record in self:
            record.display_name = '%s %s' % (record.name, record.lastname)

class ResUsers(models.Model):
    _inherit = 'res.users'

    profesor_id = fields.Many2one('school.profesor', string='Profesor Asociado')