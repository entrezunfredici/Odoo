# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic
#Module database model
from odoo import fields, models

class Property_tags(models.Model):
    _name="estate.property.tags"
    _description="Property tags, contain informations about property tags"
    name=fields.Char("name", required=True)