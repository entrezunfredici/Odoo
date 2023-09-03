# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic
#Module database model
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class Property_offer(models.Model):
    #"fields
    _name="estate.property.offer"
    _description="property offers, contains estate offers"
    _order="price desc" #order in lists
    price=fields.Float("price")
    status=fields.Selection(
        string='status',
        selection=[
            ('Accepted','Accepted'),
            ('Refused','Refused')
        ]
    )
    validity=fields.Integer("validity", default=7)
    #linked fields
    partner_id=fields.Many2one('res.partner', string='partner', required='true')
    property_id=fields.Many2one('estate.property', string='property', required='true')
    property_type_id=fields.Many2one('estate.property.type', string='property type') #12.3. status buttons; property type
    #computed fields
    date_deadline=fields.Date(compute="_compute_date_deadline", inverse="_inverse_date_deadline")
    #computed functions
    @api.depends("create_date", "validity")
    def _compute_date_deadline(self):
        for offer in self:
            date=offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.date_deadline=date+relativedelta(days=offer.validity)
    def _inverse_date_deadline(self):
        for offer in self:
            date=offer.create_date.date() if offer.create_date else fields.Date.today()
            offer.validity=(offer.date_deadline-date).days
    #button functions
    def estate_property_offer_action_Accept(self):
        for offer in self:
            offer.status="Accepted"
            offer.property_id.selling_price=offer.price
            offer.property_id.state="Offer Accepted"
    def estate_property_offer_action_Refuse(self):
        for offer in self:
            offer.status="Refused"
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