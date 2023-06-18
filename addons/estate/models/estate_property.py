# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic
#Module database model
from odoo import fields, models

class Property(models.Model):
    _name="estate.property"
    _description="Property model, contain informations about estate properties"
    #basic fields on hte table
    name=fields.Char(required=True) #required fields
    description=fields.Text()
    postcode=fields.Char()
    date_availability=fields.Date()
    expected_price=fields.Float(required=True) #required fields
    selling_price=fields.Float()
    bedrooms=fields.Integer()
    living_area=fields.Integer()
    facades=fields.Integer()
    garage=fields.Boolean()
    garden=fields.Boolean()
    garder_area=fields.Integer()
    garden_orientation=fields.Selection(
        string='type',
        selection=[('north','North'),('south','South'),('est','Est'),('West','West')],
        help="Type is used to choose garden orientation"
    )