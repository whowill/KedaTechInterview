from odoo import http
from odoo.http import request, Response
from werkzeug.exceptions import NotFound
import json

class MaterialManagementController(http.Controller):
    
    @http.route('/api/materials', auth='public', type='http', methods=['GET'], csrf=False)
    def get_materials(self, **kwargs):
        material_type = kwargs.get('type')
        domain = []
        if material_type:
            domain.append(('type', '=', material_type))
        materials = request.env['material.management'].sudo().search_read(
            domain, ['type', 'material_name', 'buy_price']
        )
        return Response(
            json.dumps({'status': 'success', 'data': materials}),
            content_type='application/json',
            status=200
        )


    @http.route('/api/material_update/<int:material_id>', type='json', auth='public', methods=['PUT'], csrf=False)
    def update_material(self, material_id, **kwargs):
        material = request.env['material.management'].sudo().browse(material_id)
        if not material.exists():
            raise NotFound("Material not found")
        
        material.write(kwargs)
        return {'status': 'success', 
                'message': 'Material updated successfully'}
        

    @http.route('/api/material_delete/<int:material_id>', type='json', auth='public', methods=['DELETE', 'POST'], csrf=False)
    def delete_material(self, material_id, **kwargs):
        material = request.env['material.management'].sudo().browse(material_id)
        if not material.exists():
            return NotFound("Material not found")
        material.unlink()
        return {'status': 'success', 'message': 'Material deleted successfully'}
    
        