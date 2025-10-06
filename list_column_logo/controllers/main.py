from odoo import http
from odoo.http import request


class ListColumnLogoController(http.Controller):
    @http.route('/list_column_logo/get_logos', type='json', auth='user')
    def get_logos(self, model, fields):
        if not fields:
            return {}
        result = {}
        # Fetch via logo model only, using its related field to filter
        logos = request.env['ir.model.field.logo'].sudo().search([
            ('field_id.model', '=', model), ('field_id.name', 'in', fields)
        ])
        for logo in logos:
            # Prefer a medium size for headers; fall back to original if missing
            img = logo.image_256 or logo.image_128 or logo.image_512 or logo.image_1024 or logo.image_1920
            if img and logo.field_id and logo.field_id.name:
                result[logo.field_id.name] = img
        return result
