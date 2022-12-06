# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Hospital Management',
    'version': '1.0.0',
    'category': 'Hospital',
    'sequence': -100,
    'summary': 'Hospital management system',
    'description': "This is the first module",
    'depends': [
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/hospital_patient_view.xml',
        'views/female_patient_view.xml',
        'views/menu.xml',
    ],
    'demo': [],
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}