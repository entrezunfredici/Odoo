# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic
#Module database model
from odoo import fields, models

class Property(models.Model):
    _name="estate.property"
    _description="Property model, contain informations about estate properties"
    active = fields.Boolean("Active", default=False)
    #basic fields on the table
    name=fields.Char("name", required=True) #required fields
    description=fields.Text("description")
    postcode=fields.Char("postcode")
    date_availability=fields.Date("Available From", copy=False, default=lambda self: fields.Datetime.today())
    expected_price=fields.Float("price", required=True) #required fields
    selling_price=fields.Float("selling price", copy=False, readonly=True)
    bedrooms=fields.Integer("bedrooms", default=2)
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
    #state of estate property
    state=fields.Selection(
        string='state',
        selection=[
            ('New','New'),
            ('Offer Received','Received'),
            ('Offer Accepted','Accepted'),
            ('Sold and canceled','Sold')
        ],
        default='New'
    )
    user_id = fields.Many2one('res.users', string='user')
    partner_id=fields.Many2one('res.partner', string="partner")
    property_type_id=fields.Many2one('estate.property.type', string="property.type")
    property_tags_ids=fields.Many2many("estate.property.tags", string="property.type")