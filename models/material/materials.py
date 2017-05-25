# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Materials(models.Model):
	_name = 'philsteel.materials'


	image = fields.Binary()
	name = fields.Char(string="Material Name", required='True')
	code = fields.Char(string="Code")
	description = fields.Text(string="Description")
	prices = fields.Float(string='Material Price')


class Materiales(models.Model):
	_name = 'philsteel.materiales'

	image = fields.Binary()
	name = fields.Many2one(
		'philsteel.materials', 'Material Name',  ondelete='cascade', required='True'
	)
	quantity_installed = fields.Integer(string='Quantity', required='True')