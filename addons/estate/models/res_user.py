# -*- coding: utf-8 -*-
#Real Estate Odoo module created by Macabiau Frederic

# 1 : imports of odoo
from odoo import fields, models

class ResUser(models.Model):
    #private attributes
    _inherit="res.user"#inheritage
    
    #fields declkaration
    property_ids=fields.One2many("estate.property","res_user_id",string="lists available property")


