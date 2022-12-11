# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'khaikal_academy.course'

    name = fields.Char(string='Title', required=True)
    description = fields.Text(string='Description')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
