from odoo import fields, models, api


class KhachHang(models.Model):
    _name = 'khach.hang'
    _description = 'Model thông tin Khách Hàng'

    name = fields.Char(string='Name', required=True)
    phone = fields.Char(string='Phone number')
    email = fields.Char(string='Email')
    contact = fields.Char(string='Contact')
    img = fields.Binary()
    loyalty_point = fields.Float(string='Loyalty point', readonly=1)
    loyalty_level = fields.Many2one( 'partner.levels', string='Partner levels', readonly=1)
