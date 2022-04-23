from odoo import fields, models, api


class PartnerLevels(models.Model):
    _name = 'partner.levels'
    _description = 'Model Partner Levels'

    name = fields.Char(string='Partner level', required=True)
    loyalty_points = fields.Float(string='Loyalty points', required=True)
    description = fields.Text(string='Description')

