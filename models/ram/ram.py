

from odoo import models, fields, api, _


class RAM(models.Model):
     _name = 'philsteel.ram'

     customer = fields.Char(string='Client', required='True')

     ram_number = fields.Char(string='RAM Number', required='True')
     location = fields.Text(string='Address', required='True')

     name = fields.Many2one(
         'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
     )

     project_type = fields.Selection([('residential', 'Residential'), ('commercial', 'Commercial'), ('industrial', 'Industrial'), ('government', 'Government'), ('institutional', 'Institutional'), ('mass_housing', 'Mass Housing')], string='Type of Project', required='True')

  
     product_profile = fields.Many2many('philsteel.materiales', string='Product Profile', required='True',  ondelete='cascade')


     work_scope = fields.Many2many('philsteel.workscope', string='Scope of Work',  ondelete='cascade')

   
     received_datetime = fields.Datetime(string='Date / Time Received')
     date_received_measurement = fields.Date(string='Date receive measurement',)
     date_sr_received = fields.Date(string='Date SR measurement')
     area_manager = fields.Many2one(
        'philsteel.projectmanpower', 'Area Manager',  ondelete='cascade', required='True'
     )
     client_rep = fields.Many2one(
        'philsteel.contacts', 'Sales Representative',  ondelete='cascade', required='True'
     )
     project_sector = fields.Many2one(
         'philsteel.projectsector', 'Project Sector',  ondelete='cascade', required='True'
     )
     remarks = fields.Text(string="Remarks")
    
     #image = fields.Binary()
     statuss = fields.Selection([
         ('draft', 'Draft'),
         ('approved', 'Approved'),
         ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')

     @api.onchange('name')
     def get_proj_details(self):
         for record in self:
             record.customer = record.name.customer_name
             record.location = record.name.location
             record.project_type = record.name.types_of_project
             record.area_manager = record.name.area_manager
             record.client_rep = record.name.client_rep

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

