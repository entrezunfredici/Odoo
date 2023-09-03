# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic
#Module database model
from odoo import api, fields, models
import statistics

class Property_type(models.Model):
    _name="estate.property.type"
    _description="Property type, contain informations about property type"
    _order="sequence, name"
    #basic fields on the table
    name=fields.Char("name", required=True) #required fields
    sequence=fields.Integer("Sequence", default=1, help="used to ordre estate porperties by types")
    #linked fields
    property_ids=fields.One2many('estate.property','property_type_id', string='property') #list of typed property
    offer_ids=fields.One2many('estate.property.offer','property_type_id', string='offers') #12.3. status buttons; List of offers 
    #conputed fields
    property_count=fields.Integer(compute="_compute_property_counter")
    offer_count=fields.Integer(compute="_compute_offers_counter")
    #computed functions
    @api.depends("property_ids")
    def _compute_property_counter(self):
        for property_type in self:
            Expected_Price_Sum=sum(property_type.property_ids.mapped("expected_price"))if property_type.property_ids else 0.0
            Expected_Price_Mean=statistics.mean(property_type.property_ids.mapped("expected_price"))if property_type.property_ids else 1.0
            property_type.property_count=int(Expected_Price_Sum/Expected_Price_Mean)
    @api.depends("offer_ids")
    def _compute_offers_counter(self):
        for property_type in self:
            Price_Sum=sum(property_type.offer_ids.mapped("price"))if property_type.offer_ids else 0.0
            Price_Mean=statistics.mean(property_type.offer_ids.mapped("price"))if property_type.offer_ids else 1.0
            property_type.offer_count=int(Price_Sum/Price_Mean)
    #constraints
    _sql_constraints=[
        ('check_estate_property_property_type_name','UNIQUE(name)','the type name can be unique')
    ]
