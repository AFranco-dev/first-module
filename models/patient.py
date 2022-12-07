# -*- coding: utf-8 -*-
from odoo import api, fields, models
from datetime import date


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = 'Hospital Patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    name = fields.Char(string='Name', tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age', tracking=True)
    gender = fields.Selection([('male','Male'),('female','Female')], string="Gender", tracking=True)
    ref = fields.Char(string='Reference')
    active = fields.Boolean(string='Active', default=True)
    date_of_birth = fields.Date(string="Date Of Birth")

    def _compute_age(self):
        today = date.today()
        this_year_birthday = date(today.year, self.date_of_birth.month, self.date_of_birth.day)
        if this_year_birthday < today:
            self.age = today.year - self.date_of_birth.year
        else:
            self.age = today.year - self.date_of_birth.year - 1