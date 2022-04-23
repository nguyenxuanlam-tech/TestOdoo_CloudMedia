# -*- coding: utf-8 -*-

from odoo import models, fields, api


class LoyaltySale(models.Model):
    # _name = 'loyalty.sale'
    _inherit='sale.order'
    _description = 'Model info Loyalty Sale'

    loyalty_for_sale_id = fields.Many2one('loyalty.program', string='Loyalty id')