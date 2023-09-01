# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic
#Module database model
from odoo import fields, models

class Property_tags(models.Model):
    _name="estate.property.tags"
    _description="Property tags, contain informations about property tags"
    _order="name" #order in lists
    name=fields.Char("name", required=True)
    Color=fields.Integer("color")
    _sql_constraints=[
        ('check_estate_property_property_tags_name','UNIQUE(name)','the tag name can be unique')
    ]