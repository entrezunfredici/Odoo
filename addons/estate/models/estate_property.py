# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic
#Module database model
from odoo import api, fields, models
from odoo.exceptions import UserError
from dateutil.relativedelta import relativedelta

class Property(models.Model):
    _name="estate.property"
    _description="Property model, contain informations about estate properties"
    _order="id desc"
    active = fields.Boolean("Active", default=True)
    #basic fields on the table
    name=fields.Char("name", required=True) #required fields
    description=fields.Text("description")
    postcode=fields.Char("postcode")
    date_availability=fields.Date("Available From", copy=False, default=lambda self: (fields.Datetime.today()))
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
            ('Offer Received','Offer Received'),
            ('Offer Accepted','Offer Accepted'),
            ('Sold','Sold'),
            ('Canceled','Canceled')
        ],
        default='New'
    )
    #linked fields
    user_id = fields.Many2one('res.users', string='user')
    partner_id=fields.Many2one('res.partner', string="partner")
    property_type_id=fields.Many2one('estate.property.type', string="property.type")#type of this property
    property_tags_ids=fields.Many2many("estate.property.tags", string="property.tags")#tags list of this property
    offer_ids=fields.One2many("estate.property.offer", "property_id", string="property offer")#offers list of this property
    #computed variable
    total_area=fields.Float(compute="_compute_total_area")
    best_price=fields.Float(compute="_compute_best_price")#more expensive offer
    #compute functions
    @api.depends("living_area","garden_area")
    def _compute_total_area(self):
        for estate_property in self:
            estate_property.total_area=estate_property.living_area+estate_property.garden_area
    @api.depends("offer_ids")
    def _compute_best_price(self):
        for estate_property in self:
            estate_property.best_price=max(estate_property.offer_ids.mapped("price")) if estate_property.offer_ids else 0.0
    #onchange functions
    @api.onchange("garden")
    def _onchange_garden(self):
        if self.garden:
            self.garden_area=10
            self.garden_orientation="N"
        else:
            self.garden_area=0
            self.garden_orientation=False
    #buttons functions
    def estate_property_action_cancel(self):
        for estate_property in self:
            if(estate_property.state=="Sold"):
                raise UserError('Sold property cannot be canceled')
            else:
                estate_property.state="Canceled"
                return True
    def estate_property_action_sold(self):
        for estate_property in self:
            if(estate_property.state=="Canceled"):
                raise UserError('Canceled property cannot be sold')
            else:
                estate_property.state="Sold"
                return True
    #CRUD functions
    def ondelete(self):
        for estate_property in self:
            if(estate_property.state=="New" | estate_property.state=="Canceled"):
                return super.ondelete()
            else: raise UserError('this is not a new or Canceled property')
        
    #constraints
    _sql_constraints=[
        ('check_estate_property_expected_price', 'CHECK(expected_price>0)','The expected price should be stricktly positive'),
        ('check_estate_property_selling_price', 'CHECK(selling_price>=0)','The selling price should be positive'),
        ('check_estate_property_property_tags_name','UNIQUE(name)','the tag name can be unique')
    ]
