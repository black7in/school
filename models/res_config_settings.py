from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    #hr_employee_self_edit = fields.Boolean(string="Employee Editing", config_parameter='hr.hr_employee_self_edit')
    test_active = fields.Boolean(string="Pruebas", config_parameter='school.test_active')
    
    