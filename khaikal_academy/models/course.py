# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Course(models.Model):
    _name = 'khaikal_academy.course'
    _description

    name = fields.Char(
        string='Course Name',
        required=True,
        help='Fill course name....'
        )

    description = fields.Text(
        string='Description'
        )

    active = fields.Boolean(
        string='Active', 
        default=True
        )

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100
