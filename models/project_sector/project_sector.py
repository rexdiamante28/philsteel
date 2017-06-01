# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ProjectSector(models.Model):
	_name = 'philsteel.projectsector'

	name = fields.Char(string="Sector Name", required=True)
	description = fields.Text(string="Description")
