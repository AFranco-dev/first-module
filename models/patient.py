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

    @api.depends('date_of_birth')
    def _compute_age(self):
        for rec in self:
            if rec.date_of_birth == False or rec is None:
                rec.age = 0
            else:
                today = date.today()
                this_year_birthday = date(today.year, rec.date_of_birth.month, rec.date_of_birth.day)
                if this_year_birthday < today:
                    rec.age = today.year - rec.date_of_birth.year
                else:
                    rec.age = today.year - rec.date_of_birth.year - 1