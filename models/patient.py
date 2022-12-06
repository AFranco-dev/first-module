# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='Name', tracking='true')
    age = fields.Integer(string='Age', tracking='true')
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender", tracking='true')
    ref = fields.Char(string='Reference')
    active = fields.Boolean(string='Active', default=True)