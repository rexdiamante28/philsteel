# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Materials(models.Model):
	_name = 'philsteel.materials'


	image = fields.Binary()
	name = fields.Char(string="Material Name", required='True')
	code = fields.Char(string="Code", required='True')
	description = fields.Text(string="Description")
	prices = fields.Float(string='Material Price', required='True')

	# def create(self, cr, uid, vals, context=None):
 #        sequence = self.pool.get('ir.sequence').get(cr, uid, 'test.base.code')
 #        vals['code'] = sequence
 #        res = super(Materials, self).create(cr, uid, vals, context=context)
 #        return res


class Materiales(models.Model):
	_name = 'philsteel.materiales'

	image = fields.Binary()
	name = fields.Many2one(
		'philsteel.materials', 'Material Name',  ondelete='cascade', required='True'
	)
	quantity_installed = fields.Integer(string='Quantity', required='True')
