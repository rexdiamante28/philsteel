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
	project_seen_status = fields.Date(string='Seen Status')
	particular = fields.Char(string="Particular")
	unit = fields.Char(string="Unit")
	qty = fields.Char(string="Quantity")
	weight_factor = fields.Char(string="Weight Factor")
	#--------Previous---------#
	accomplisment = fields.Many2many('philsteel.accomplishment', string='Accomplishments',  ondelete='cascade')
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
			record.customer_name = record.name.customer_name