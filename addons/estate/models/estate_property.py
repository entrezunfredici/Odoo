# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic
#Module database model
from odoo import fields, models

class Property(models.Model):
    _name="estate.property"
    _description="Property model, contain informations about estate properties"
    #basic fields on the table
    name=fields.Char("name", required=True) #required fields
    description=fields.Text("description")
    postcode=fields.Char("postcode")
    date_availability=fields.Date("Available From")
    expected_price=fields.Float("price", required=True) #required fields
    selling_price=fields.Float("selling price")
    bedrooms=fields.Integer("bedrooms")
    living_area=fields.Integer("living area")
    facades=fields.Integer("facades")
    garage=fields.Boolean("garage")
    garden=fields.Boolean("garden")
    garden_area=fields.Integer("garden_area")
    garden_orientation=fields.Selection(
        string='garden orientation',
        selection=[
            ('N','North'),
            ('S','South'),
            ('E','Est'),
            ('W','West')
        ],
        help="Type is used to choose garden orientation"
    )