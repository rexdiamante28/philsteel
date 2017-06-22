# -*- coding: utf-8 -*-

from odoo import models, fields, api



class PISReports(models.Model):
	_name = 'philsteel.pisreports'


	client = fields.Char(string='Client', required='True')

	inspection_date = fields.Date(string='Date of Inspection', required='True')
	accomplishment_date = fields.Date(string='Accomplishment Date', required='True')
	roofing = fields.Boolean(string='Roofing')
	deckings = fields.Boolean(string='Decking')
	cladding = fields.Boolean(string='Cladding')
	other = fields.Char(string='Others')
	name = fields.Many2one(
		'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
	)
	contact_person = fields.Char(string='Contact Person')
	site_representative = fields.Many2one('philsteel.contacts', string='Representative at Site during Inspection', required='True',  ondelete='cascade')
	designation_contact = fields.Char(string='Designation Contact ')
	location = fields.Char(string='Location', required='True')
	ic_number = fields.Char(string='I.C Number')
	sc_number = fields.Char(string='S.C Number')
	arrival_time = fields.Datetime(string='Time of Arrival', required='True')
	departure_time = fields.Datetime(string='Time of Departure', required='True')
	
	work_scope = fields.Many2many('philsteel.workscope', string='Scope of Work',  ondelete='cascade')
	activity = fields.Many2many('philsteel.projectactivities', string='Activities',  ondelete='cascade', required='True')
	material = fields.Many2many('philsteel.materiales', string='Materials Installed',  ondelete='cascade')
	wheather = fields.Selection([('rainy', 'Rainy'), ('cloudy', 'Cloudy'), ('fair', 'Fair')], string='Weather', required='True')

	other_concerns = fields.Text(string="Other concerns:")

	prepared_by = fields.Many2one(
		'philsteel.contacts', 'Prepared By',  ondelete='cascade'
	)
	approved_by = fields.Many2one(
		'philsteel.contacts', 'Noted By',  ondelete='cascade'
	)
	assignedTo = fields.Many2one(
         'philsteel.android', 'Assigned To',  ondelete='cascade'
     )
	assigned_by = fields.Many2one(
         'res.users', 'Assigned By',  ondelete='cascade', required='True'
     )
	project_sector = fields.Many2one(
         'philsteel.projectsector', 'Project Sector',  ondelete='cascade', required='True'
     )

	foreman = fields.Integer(string='Foreman')
	leadman = fields.Integer(string='Leadman')
	tinsmith = fields.Integer(string='Tinsmith')
	installer = fields.Integer(string='Installer')
	welder = fields.Integer(string='Welder')
	helper = fields.Integer(string='Helper')
	site_address = fields.Text(string="Jobsite Address")
	site_sketch = fields.Binary(string='Jobsite Sketch')
	seen_datetime = fields.Datetime(string='Seen')
	read_datetime = fields.Datetime(string='Read')
	pisimages = fields.One2many('philsteel.inspectionimages', 'inspection', string="Inspection and Safety Report Images")
	tool_equipment = fields.Many2many('philsteel.materials', string='Tools and Equipments',  ondelete='cascade')
	statuss = fields.Selection([
		('draft', 'Draft'), 
		('approved', 'Approved'),
		], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')


	@api.onchange('name')
	def get_proj_details(self):
		for record in self:
			record.client = record.name.customer_name
			record.ic_number = record.name.ic_no
			record.sc_number = record.name.sc_no
			record.location = record.name.location
			

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


class PISImages(models.Model):
	_name = 'philsteel.inspectionimages'

	name = fields.Binary(string='Image')
	description = fields.Text(string='Description')

	inspection = fields.Many2one('philsteel.pisreports',
		ondelete='cascade', string="Inspection and Safety Report", required=True)

	location = fields.Char(string="Map Location")
	taken = fields.Datetime(string='Date/Time Taken')
	# datetime_taken = fields.Datetime(string ='Date/Time Taken')
