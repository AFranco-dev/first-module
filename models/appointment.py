# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Hospital Appointment'