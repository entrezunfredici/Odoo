from odoo import fields, models
from odoo import models

class Property(models.Model):
    _name="estate.property"
    _description="Property model, contain informations about estate properties"
    name=fields.Char()