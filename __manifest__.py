{
    'name': 'Material Management',
    'version': '1.0',
    'category': 'Inventory',
    'sequence': 1,
    'summary': 'Material Management System',
    'author': 'Cholid Fitra Fahriza',
    'depends': [
        'base',
    ],
    'description': "Keda tech take home interview task",
    'data': [
        'views/material_management_views.xml',
        'views/material_supplier_views.xml',
        'views/menu_views.xml',
        'security/ir.model.access.csv',
    ],
    'demo': [],
    'qweb': [],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}