# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LoyaltyProgram(models.Model):
    _name = 'loyalty.program'
    _description = 'Model info Loyalty Program.'

    name = fields.Char(string='Name Program', required=True)
    points = fields.Float(string='Points', required=True)
    active = fields.Boolean(string='Active', required=True)
    description = fields.Text(string='Description')

#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
