from odoo.tests.common import HttpCase, tagged
import requests
import json

@tagged('post_install', '-at_install')
class TestMaterialController(HttpCase):

    def test_get_materials(self):
        supplier = self.env['material.supplier'].create({'name': 'Supplier A'})
        material = self.env['material.management'].create({
            'material_code': 'C005',
            'material_name': 'Get Material Name',
            'type': 'cotton',
            'buy_price': 150.0,
            'material_supplier_id': supplier.id,
        })

        response = self.url_open(f'/api/materials?type=cotton')
        data = json.loads(response.content.decode())
        


    def test_update_material(self):
        supplier = self.env['material.supplier'].create({'name': 'Supplier A'})
        material = self.env['material.management'].create({
            'material_code': 'C006',
            'material_name': 'Update Material Name',
            'type': 'cotton',
            'buy_price': 150.0,
            'material_supplier_id': supplier.id,
        })
        url = f'http://localhost:8069/api/material_update/{material.id}'
        update_data = {
            'material_code': 'C007',
            'material_name': 'Updated Name',
            'type': 'jeans',
            'buy_price': 200.0,
            'material_supplier_id': supplier.id,
        }
        rpc_payload = {
            "jsonrpc": "2.0",
            "method": "call",
            "params": update_data,
            "id": 1
        }
        requests.put(url, json=rpc_payload)



    def test_delete_material(self):
        supplier = self.env['material.supplier'].create({'name': 'Test Supplier'})
        material = self.env['material.management'].create({
            'material_code': 'C004',
            'material_name': 'To Be Deleted',
            'type': 'cotton',
            'buy_price': 150.0,
            'material_supplier_id': supplier.id,
        })
        url = f'http://localhost:8069/api/material_delete/{material.id}'
        requests.delete(url, json={})
        
