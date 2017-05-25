# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PAS(models.Model):
	_name = 'philsteel.pas'

	updated_as_of = fields.Date(string='Updated as of')
	name = fields.Many2one(
		'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
	)
	customer_name = fields.Text(string="")
	location = fields.Text(string="Location")
	ic_no = fields.Char(string="I.C. No:")
	sc_no = fields.Char(string="S.C. No:")
	duration = fields.Char(string="Duration" , required=True)
	date_start = fields.Date(string='Date of Started')
	date_complete = fields.Date(string='Target Date of Completion')
	sales_engineer = fields.Many2one(
		'philsteel.contacts', 'Personnel',  ondelete='cascade'
	)
	#---------------------------------------------------#
	accomplisment = fields.Many2many('philsteel.accomplishment', string='Accomplishments',  ondelete='cascade')
	particular = fields.Char(string="Particular")
	unit = fields.Char(string="Unit")
	qty = fields.Char(string="Quantity")
	weight_factor = fields.Char(string="Weight Factor")
	#--------Previous---------#
	qty_prev = fields.Char(string="Quantity")
	percent_prev = fields.Char(string="Percentage")
	#--------This Period---------#
	qty_thisperiod = fields.Char(string="Quantity")
	percent_thisperiod = fields.Char(string="Percentage")
	#--------To Date---------#
	qty_todate = fields.Char(string="Quantity")
	percent_todate = fields.Char(string="%")
	weight = fields.Char(string="Weight Percent")
	assignedTo = fields.Many2one(
         'philsteel.android', 'Assigned To',  ondelete='cascade'
     )


	seen_datetime = fields.Datetime(string='Seen')
	read_datetime = fields.Datetime(string='Read')
	#----------------------------------------------------#
	remarks = fields.Text(string="Remarks")
	proj_incharge = fields.Many2one(
		'philsteel.contacts', 'Project In Charge',  ondelete='cascade'
	)
	client_rep = fields.Many2one(
		'philsteel.contacts', 'Client Representative',  ondelete='cascade'
	)
	site_address = fields.Text(string="Jobsite Address")
	site_sketch = fields.Binary(string='Jobsite Sketch')

	accomplishmentimages = fields.Many2many('philsteel.accomplishmentimages', string='Accomplishment Images',  ondelete='cascade')

	statuss = fields.Selection([
		('draft', 'Draft'), 
		('approved', 'Approved'),
		], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
	

	@api.multi
	def action_approved(self):
		for visit in self:
			visit.statuss = 'approved'

		return True


	@api.onchange('name')
	def get_proj_details(self):
		for record in self:
			record.location = record.name.location
			record.ic_no = record.name.ic_no
			record.sc_no = record.name.sc_no
			record.sc_no = record.name.sc_no

class AccomplishmentImages(models.Model):
	_name = 'philsteel.accomplishmentimages'

	name = fields.Binary(string='Image')
	description = fields.Text(string='Description')

	accomplishment = fields.Many2one('philsteel.pas',
		ondelete='cascade', string="Project Accomplsihment", required=True)

	new_field = fields.Binary()