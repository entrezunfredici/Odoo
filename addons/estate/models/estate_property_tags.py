# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic

# 1 : imports of odoo
from odoo import fields, models

class Property_tags(models.Model):
    #private attributes 
    _name="estate.property.tags"
    _description="Property tags, contain informations about property tags"
    _order="name" #order in lists

    #fields declaration
    name=fields.Char("name", required=True)
    Color=fields.Integer("color")
    
    #constraints
    _sql_constraints=[
        ('check_estate_property_property_tags_name','UNIQUE(name)','the tag name can be unique')
    ]