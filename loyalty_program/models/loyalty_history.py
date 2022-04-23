from odoo import fields, models, api


class LoyaltyHistory(models.Model):
    _name = 'loyalty.history'
    _description = 'Model Loyalty History'

    partner_id = fields.Many2one('khach.hang')
    loyalty_points = fields.Float(string='Loyalty points')
    money_spent = fields.Float(string='Money spent')
    loyalty_point = fields.Float(string='Loyalty point', readonly=True)
    date_order = fields.Datetime(string='Date order')
    order_id = fields.Char(string='Order id')