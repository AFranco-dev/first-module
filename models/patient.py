# -*- coding: utf-8 -*-
from odoo import api, fields, models


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    name = fields.Char(String='Name')
    age = fields.Integer(String='Age')
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender")
    