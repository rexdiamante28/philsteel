# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Accomplishments(models.Model):
	_name = 'philsteel.accomplishment'

	name = fields.Char(string="Particular")
	unit = fields.Char(string="Unit")
	qty = fields.Char(string="Quantity")
	weight_factor = fields.Char(string="Weight Factor")
	#--------Previous---------#
	qty_prev = fields.Char(string="Previous Quantity")
	percent_prev = fields.Char(string="Previous Percentage")
	#--------This Period---------#
	qty_thisperiod = fields.Char(string="This Period Quantity")
	percent_thisperiod = fields.Char(string="This Period Percentage")
	#--------To Date---------#
	qty_todate = fields.Char(string="This Date Quantity")
	percent_todate = fields.Char(string="This Date Percent")
	weight = fields.Char(string="Weight Percent")
	#----------------------------------------------------#
	remarks = fields.Text(string="Remarks")