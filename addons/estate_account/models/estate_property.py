# -*- coding: utf-8 -*-
#Estate_account Odoo module created by Macabiau Frederic
from odoo import models, fields, Command

class estate_property(models.Model):
    _inherit="estate.property"
    def estate_property_action_sold(self):
        account_ids=fields.Many2one('account.move')
        """ When an invoice linked to a sales order selling registrations is
        paid confirm attendees. Attendees should indeed not be confirmed before
        full payment. """
        price=fields.Integer("price")
        price=int(self.selling_price*1.06+100.00)
        account_ids.account=self.partner_id
        account_ids.move_type='out_invoyce',
        self.env["account.move"].create(
            {
                "name":"account.move",
                "line_ids":[
                    Command.create({
                        "name": "self.name",
                        "quantity": "1",
                        "price_unit": price
                    })
                ],
            }
        )
        return super().estate_property_action_sold()