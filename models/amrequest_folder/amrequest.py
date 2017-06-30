

from odoo import models, fields, api, _


class AMRequests(models.Model):
     _name = 'philsteel.amrequests'

     customer = fields.Char(string='Customer', required='True')

     status = fields.Selection([('new', 'New'), ('visited', 'Visited')], default='new', string='Request Status')

     illustrations = fields.One2many('philsteel.amrimages', 'rfam', string="Illustrations")


     request_number = fields.Char(string='Request Number', required='True')
     location = fields.Text(string='Address', required='True')

     name = fields.Many2one(
         'philsteel.projects', 'Project Name',  ondelete='cascade', required='True'
     )

     project_type = fields.Selection([('residential', 'Residential'), ('commercial', 'Commercial'), ('industrial', 'Industrial'), ('government', 'Government'), ('institutional', 'Institutional'), ('mass_housing', 'Mass Housing')], string='Type of Project', required='True')
     project_site_address = fields.Text(string='Complete Project Site Address')
     project_site_sketch = fields.Binary(string='Jobsite Sketch')
     general_contractor = fields.Char(string='Name of Contractor')


     contact_person_at_site = fields.Many2many('philsteel.contacts', string='Site Contact Person', required='True',  ondelete='cascade')
     jobsite_contact_number = fields.Char(string='Job Site Telephone or Mobile Number', required='True')
     product_profile = fields.Many2many('philsteel.materiales', string='Product Profile', required='True',  ondelete='cascade')

     sc_number = fields.Char(string='SC NO')
     ic_number = fields.Char(string='IC NO')
     sq_number = fields.Char(string='SQ NO')
     iq_number = fields.Char(string='IQ NO')

     work_scope = fields.Many2many('philsteel.workscope', string='Scope of Work',  ondelete='cascade')

     frames_trusses_installed = fields.Char(string='% Frames / Trusses Installed')
     purlins_installed = fields.Char(string='% Purlins Installed')
     sogrod_installed = fields.Char(string='% Sagrod Installed')
     beam_installed = fields.Char(string='% Beam Installed')
     floors_available_for_measurement = fields.Char(string='% No. of Floors Available for Measurement')

     rfm_quotation = fields.Boolean(string='Quotation')
     rfm_contract = fields.Boolean(string='Contract')
     rfm_fabrication = fields.Boolean(string='Fabrication')
     rfm_tech1assistance = fields.Boolean(string='Tech 1 Assistance')
     rfm_others = fields.Text(string='Others')

     ready_for_measurement_date = fields.Date(string='Date when structure ready for measurement', required='True')
     seen_datetime = fields.Datetime(string='Seen')
     read_datetime = fields.Datetime(string ='Read')
     accomplished_by = fields.Many2one(
         'philsteel.android', 'Accomplished By',  ondelete='cascade'
     )

     date_filed = fields.Date(string='Date Filed')

     approved_by = fields.Many2one(
         'res.users', 'Approved By',  ondelete='cascade'
     )
     assigned_by = fields.Many2one(
         'res.users', 'Assigned By',  ondelete='cascade', required='True'
     )

     assignedTo = fields.Many2one(
         'philsteel.android', 'Assigned To',  ondelete='cascade'
     )
     project_sector = fields.Many2one(
         'philsteel.projectsector', 'Project Sector',  ondelete='cascade', required='True'
     )
     proj_incharge = fields.Many2one(
        'philsteel.projectmanpower', 'Project In-charge',  ondelete='cascade'
     )
     area_manager = fields.Many2one(
        'philsteel.projectmanpower', 'Area Manager',  ondelete='cascade'
     )
     fore_man = fields.Many2one(
        'philsteel.projectmanpower', 'Foreman Assigned',  ondelete='cascade'
     )
     client_rep = fields.Many2one(
        'philsteel.contacts', 'Sales Representative',  ondelete='cascade'
     )
     ic_amount = fields.Float(string='Installation Contract Amount ')
     sc_amount = fields.Float(string='Sales Contract Amount ')
     labor_award = fields.Float(string='Labor Award ')


     #image = fields.Binary()
     statuss = fields.Selection([
         ('draft', 'Draft'),
         ('approved', 'Approved'),
         ('ongoing', 'Ongoing'),
         ('done', 'Done'),
         ], string='Status', readonly=True, copy=False, index=True, track_visibility='onchange', default='draft')

     @api.onchange('name')
     def get_proj_details(self):
         for record in self:
             record.customer = record.name.customer_name
             record.ic_number = record.name.ic_no
             record.sc_number = record.name.sc_no
             record.location = record.name.location
             record.project_type = record.name.types_of_project
             record.proj_incharge = record.name.proj_incharge
             record.area_manager = record.name.area_manager
             record.fore_man = record.name.fore_man
             record.client_rep = record.name.client_rep
             record.ic_amount = record.name.ic_amount
             record.sc_amount = record.name.sc_amount
             record.labor_award = record.name.labor_award

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



     @api.multi
     def action_ongoing(self):
         for visit in self:
             visit.statuss = 'ongoing'

         return True


     @api.multi
     def action_done(self):
         for visit in self:
             visit.statuss = 'done'

         return True

     # @api.model
     # def create(self, values):
         
     #     if values.get('request_number', 'New') == 'New':
     #         values['request_number'] = self.env['ir.sequence'].next_by_code('philsteel.amrequests') or 'New'

     #     result = super(AMRequests, self).create(values)

     #     return result





class AMRImages(models.Model):
    _name = 'philsteel.amrimages'

    name = fields.Binary(string='Image')
    description = fields.Text(string='Description')
    rfam = fields.Many2one('philsteel.amrequests',
        ondelete='cascade', string="RFM", required='True')
    location = fields.Char(string='Map Location')
    taken = fields.Datetime(string='Date/Time Taken')

    

