from odoo import fields, models, api


class ConfigSetting(models.TransientModel):
    _inherit = 'res.config.settings'
    _description = 'Model Config Setting'

    loyalty_email_notify = fields.Boolean(default=False)
