# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic
#Module database model
from odoo import api, fields, models
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError

class Property_offer(models.Model):
    _name="estate.property.offer"
    _description="property offers, contains estate offers"
    price=fields.Float("price")
    status=fields.Selection(
        string='status',
        selection=[
            ('Accepted','Accepted'),
            ('Refused','Refused')
        ]
    )
    partner_id=fields.Many2one('res.partner', string='partner', required='true')
    property_id=fields.Many2one('estate.property', string='property', required='true')
    validity=fields.Integer("validity", default=7)
    #computed variables
    #date_deadline=fields.Date(compute="_compute_create_date", inverse="_inverse_date_deadline")
    #date_validity=fields.Date()
    #compute functions
    #@api.depends("")
    #def _compute_date_deadline(self):
    #    for offer in self:
    #        offer.date_deadline=fields.Datetime.today()#+relativedelta(mounth=3)
    #def _inverse_date_deadline(self):
    #    for offer in self:
    #        offer.date_validity=relativedelta(days=7)
            #offer.date_validity=offer.date_deadline-fields.Datetime.today()
    #button functions
    def estate_property_offer_action_Accept(self):
        for offer in self:
            offer.status="Accepted"
            offer.property_id.selling_price=offer.price
            offer.property_id.state="Sold"
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