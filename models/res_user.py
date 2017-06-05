

from odoo import models, fields, api


class User(models.Model):

    _inherit = 'res.users'

    sector = fields.Selection([('none', 'None'), ('north_1', 'North 1 Sector'), ('north_2', 'North 2 Sector'), ('south', 'South Sector')], default='none', string='Sector')

    