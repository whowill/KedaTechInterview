from odoo import models, fields, api
from odoo.exceptions import ValidationError

class MaterialSupplier(models.Model):
    _name = 'material.supplier'
    _description = 'Material Supplier'

    name = fields.Char(string='Supplier Name', required=True)

class MaterialManagement(models.Model):
    _name = 'material.management'
    _description = 'Material Management'

    material_code = fields.Char(string='Material Code', required=True)
    material_name = fields.Char(string='Name', required=True)
    type = fields.Selection([
        ('fabric', 'Fabric'),
        ('jeans', 'Jeans'),
        ('cotton', 'Cotton')
    ], string='Material Type', required=True)
    buy_price = fields.Float(string='Buy Price', required=True, default=100.0)
    material_supplier_id = fields.Many2one('material.supplier', string='Supplier', required=True)

    @api.constrains('buy_price')
    def _check_buy_price(self):
        for record in self:
            if record.buy_price < 100:
                raise ValidationError("Buy price must be greater or equal to 100.")
            
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.material_code} - {record.material_name}"
            result.append((record.id, name))
        return result