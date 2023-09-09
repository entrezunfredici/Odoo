# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic

# 1 : import of python lib
from dateutil.relativedelta import relativedelta
#2: import of odoo
from odoo import api, fields, models
from odoo.exceptions import ValidationError

class Property_offer(models.Model):
    #private attributes
    _name="estate.property.offer"
    _description="property offers, contains estate offers"
    _order="price desc" #order in lists
    
    #fields declaration
    price=fields.Float("price")
    status=fields.Selection(
        string='status',
        selection=[
            ('Accepted','Accepted'),
            ('Refused','Refused')
        ]
    )
    validity=fields.Integer("validity", default=7)
    partner_id=fields.Many2one('res.partner', string='partner', required='true')
    property_id=fields.Many2one('estate.property', string='property', required='true')
    property_type_id=fields.Many2one('estate.property.type', string='property type') #12.3. status buttons; property type
    date_deadline=fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    
    #compute and search functions
    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for offer in self:
            date=offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.date_deadline=date+relativedelta(days=offer.validity)
    def _inverse_date_deadline(self):
        for offer in self:
            date=offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.validity=(offer.date_deadline-date).days
    
    #constraints
    _sql_constraints=[
        ('check_estate_property_offer_price','CHECK(price>0)','The offer price must be stricktly posivite')
    ]
    @api.constrains('price')
    def check_Price(self):
        for offer in self:
            if offer.price<(0.9*offer.property_id.expected_price):
                raise ValidationError("The price offer cannot be lower ninety percent of the expected price")
            elif offer.price<max(offer.property_id.offer_ids.mapped("price")):
                raise ValidationError("The price offer can be higher than "+str(max(offer.property_id.offer_ids.mapped("price"))))
            else: offer.property_id.state="Offer Received"
    
    #action methods
    def estate_property_offer_action_Accept(self):
        for offer in self:
            offer.status="Accepted"
            offer.property_id.selling_price=offer.price
            offer.property_id.state="Offer Accepted"
    def estate_property_offer_action_Refuse(self):
        for offer in self:
            offer.status="Refused"