# -*- coding: utf-8 -*-
{
    'name': "commission_ssibtr",

    'summary': """
        Commission module for the sale's app""",

    'description': """
        Ease the load on the sale order module and organize inside data better
    """,

    'author': "SSIBTR - Kristenn Quemener",
    'website': "https://ssibtr.odoo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Sales',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'product'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/employee.xml',
        'views/automated_action.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
