from odoo import fields, models


class IrModelFieldLogo(models.Model):
    _name = 'ir.model.field.logo'
    _description = 'Field Logo for List Column'
    _rec_name = 'field_id'
    _inherit = ['image.mixin']

    field_id = fields.Many2one('ir.model.fields', required=True, ondelete='cascade', index=True)

    _sql_constraints = [
        ('field_unique', 'unique(field_id)', 'A logo already exists for this field.'),
    ]
