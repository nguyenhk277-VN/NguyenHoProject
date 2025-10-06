from odoo import models


class IrModelFields(models.Model):
	_inherit = 'ir.model.fields'

	def action_open_or_create_logo(self):
		self.ensure_one()
		Logo = self.env['ir.model.field.logo'].sudo()
		logo = Logo.search([('field_id', '=', self.id)], limit=1)
		action = {
			'type': 'ir.actions.act_window',
			'res_model': 'ir.model.field.logo',
			'view_mode': 'form',
			'target': 'current',
		}
		if logo:
			action.update({'res_id': logo.id})
		else:
			action.update({'context': {'default_field_id': self.id}})
		return action
