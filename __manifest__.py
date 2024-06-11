# -*- coding: utf-8 -*-
{
    'name': "Gestion Académica",

    'summary': "Gestión de alumnos, profesores, cursos, etc.",

    'description': """
        Módulo de gestión académica para la gestión de alumnos, profesores, cursos, etc.
        Permite la gestión de alumnos, profesores, cursos, asignaturas, notas, etc.
        Desarrollado para la asignatura de Ingeniería del Software II de la Universidad Gabriel René Moreno.
    """,

    'author': "Adrian Rosales",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Human Resources',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],
    'installable': True,
    'auto_install': False,
    'application': True,

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/entidades/alumno.xml',
        'views/entidades/tutor.xml',
        'views/planificacion/grado.xml',
        'views/planificacion/nivel.xml',
        'views/entidades/profesor.xml',
        'views/planificacion/periodo.xml',
        'views/planificacion/inscripcion.xml',
        'views/infraestructura/aula.xml',
        'views/infraestructura/bloque.xml',
        'views/planificacion/horario.xml',
        'views/planificacion/asignacion.xml',
        'views/menu.xml',
        'views/templates.xml',
        'views/res_config_settings.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

