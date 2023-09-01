# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic
#Module database model
from odoo import fields, models

class Property_type(models.Model):
    _name="estate.property.type"
    _description="Property type, contain informations about property type"
    _order="sequence, name"
    #basic fields on the table
    name=fields.Char("name", required=True) #required fields
    sequence=fields.Integer("Sequence", defaukt=1, help="used to ordre estate porperties by types")
    #linked fields
    property_ids=fields.One2many('estate.property','property_type_id', string='property') #list of typed property
    #constraints
    _sql_constraints=[
        ('check_estate_property_property_type_name','UNIQUE(name)','the type name can be unique')
    ]