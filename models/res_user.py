

from odoo import models, fields, api


class User(models.Model):

    _inherit = 'res.users'

    sector = fields.Many2one(
         'philsteel.projectsector', 'Sector (If applicable)',  ondelete='cascade'
     )

    