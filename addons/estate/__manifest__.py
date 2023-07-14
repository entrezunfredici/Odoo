# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic
#Module description
{
    "name": "Real Estate",
    'author': "Macabiau Frédéric",
    'category': 'estate',
    'version': '16.0',
    'description': """
    This is the estate app
    """,
    "depends": [
        "base",
    ],#dependencies
    "data": [
        "security/ir.model.access.csv",
        "views/estate_property_views.xml",
        "views/estate_property_type_views.xml",
        "views/estate_property_tags_views.xml",
        "views/estate_property_offer_views.xml",
        "views/estate_menus.xml",
    ],#data files
    "application": True,  # This line says the module is an App, and not a module
    "installable": True,
    "license": "LGPL-3",
}