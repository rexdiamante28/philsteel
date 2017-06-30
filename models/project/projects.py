# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Projects(models.Model):
	_name = 'philsteel.projects'

	name = fields.Char(string="Project Name", required='True')
	location = fields.Text(string="Location", required='True')
	image = fields.Binary()
	customer_name = fields.Char(string="Customer Name", required='True')
	ic_no = fields.Char(string="IC No", required='True')
	sc_no = fields.Char(string="SC No", required='True')
	types_of_project = fields.Selection([('residential', 'Residential'), ('commercial', 'Commercial'), ('industrial', 'Industrial'), ('government', 'Government'), ('institutional', 'Institutional'), ('mass_housing', 'Mass Housing')], string='Type of Project')
	proj_incharge = fields.Many2one(
		'philsteel.projectmanpower', 'Project In-charge',  ondelete='cascade', required='True'
	)
	area_manager = fields.Many2one(
		'philsteel.projectmanpower', 'Area Manager',  ondelete='cascade', required='True'
	)
	fore_man = fields.Many2one(
		'philsteel.projectmanpower', 'Foreman Assigned',  ondelete='cascade'
	)
	client_rep = fields.Many2one(
		'philsteel.contacts', 'Sales Representative',  ondelete='cascade', required='True'
	)
	ic_amount = fields.Float(string='Installation Contract Amount ', required='True')
	sc_amount = fields.Float(string='Sales Contract Amount ', required='True')
	labor_award = fields.Float(string='Labor Award ')
	

