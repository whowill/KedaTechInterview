from odoo.tests.common import TransactionCase
from odoo.exceptions import ValidationError

class TestKedaTechTakeHome(TransactionCase):

    def setUp(self):
        super(TestKedaTechTakeHome, self).setUp()
        self.MaterialSupplier = self.env['material.supplier']
        self.MaterialManagement = self.env['material.management']

        self.supplier = self.env['material.supplier'].create({
            'name': 'Test Supplier'
        })

        self.material = self.env['material.management'].create({
            'material_code': 'C001',
            'material_name': 'Test Material',
            'type': 'fabric',
            'buy_price': 150.0,
            'material_supplier_id': self.supplier.id
        })


    def test_material_management_creation(self):
        self.env['material.management'].create({
            'material_code': 'C002',
            'material_name': 'New Material',
            'type': 'jeans',
            'buy_price': 200.0,
            'material_supplier_id': self.supplier.id
        })


    def test_material_buy_price_constraint(self):
        with self.assertRaises(ValidationError):
            self.MaterialManagement.create({
                'material_code': 'C003',
                'material_name': 'Invalid Material',
                'type': 'cotton',
                'buy_price': 50.0,
                'material_supplier_id': self.supplier.id
            })

