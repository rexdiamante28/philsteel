# -*- coding: utf-8 -*-

from odoo import models, fields, api

class PAS(models.Model):
	_name = 'philsteel.pas'

	updated_as_of = fields.Date(string='Updated as of')
	name = fields.Many2one(
		'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
	)
	customer_name = fields.Text(string="", required='True')
	location = fields.Text(string="Location", required='True')
	ic_no = fields.Char(string="I.C. No:", required='True')
	sc_no = fields.Char(string="S.C. No:", required='True')
	duration = fields.Char(string="Duration")
	date_start = fields.Date(string='Date of Started')
	date_complete = fields.Date(string='Target Date of Completion')
	sales_engineer = fields.Many2one(
		'philsteel.contacts', 'Personnel',  ondelete='cascade'
	)
	#---------------------------------------------------#
	accomplisment = fields.Many2many('philsteel.accomplishment', string='Accomplishments',  ondelete='cascade')
	
	
	assignedTo = fields.Many2one(
         'philsteel.android', 'Assigned To',  ondelete='cascade'
     )
	project_sector = fields.Many2one(
         'philsteel.projectsector', 'Project Sector',  ondelete='cascade', required='True'
     )
	assigned_by = fields.Many2one(
         'res.users', 'Assigned By',  ondelete='cascade', required='True'
     )




	seen_datetime = fields.Datetime(string='Seen')
	read_datetime = fields.Datetime(string='Read')
	#----------------------------------------------------#
	
	proj_incharge = fields.Many2one(
		'philsteel.contacts', 'Project In Charge',  ondelete='cascade', required='True'
	)
	client_rep = fields.Many2one(
		'philsteel.contacts', 'Client Representative',  ondelete='cascade'
	)
	site_address = fields.Text(string="Jobsite Address")
	site_sketch = fields.Binary(string='Jobsite Sketch')
	accomplishmentimages = fields.One2many('philsteel.accomplishmentimages', 'accomplishment', string="Accomplishment Images")

	statuss = fields.Selection([
		('draft', 'Draft'), 
		('approved', 'Approved'),
		], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')
	

	@api.multi
	def action_approved(self):
		for visit in self:
			visit.statuss = 'approved'

		return True

	@api.multi
	def action_unlock(self):
		for visit in self:
			visit.statuss = 'draft'

		return True


	@api.onchange('name')
	def get_proj_details(self):
		for record in self:
			record.location = record.name.location
			record.ic_no = record.name.ic_no
			record.sc_no = record.name.sc_no
			record.customer_name = record.name.customer_name

class AccomplishmentImages(models.Model):
	_name = 'philsteel.accomplishmentimages'

	name = fields.Binary(string='Image')
	description = fields.Text(string='Description')

	accomplishment = fields.Many2one('philsteel.pas',
		ondelete='cascade', string="Project Accomplishment", required=True)

	location = fields.Char(string="Map Location")
	taken = fields.Datetime(string='Date/Time Taken')
	# datetime_taken = fields.Datetime(string ='Date/Time Taken')