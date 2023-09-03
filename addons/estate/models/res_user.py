# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic
#Module database model
from odoo import fields, models

class ResUser(models.Model):
    #inheritage
    _inherit="res.user"
    #linked fields
    property_ids=fields.One2many("estate.property","res_user_id",string="lists available property")


