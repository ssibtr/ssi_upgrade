# -*- coding: utf-8 -*-
from odoo import fields, models

class Line(models.Model):
    _inherit = 'sale.order.line'

    commission_id = fields.Many2one('sale.commission', 
        ondelete='set null', string="Sale Order", index=True)
    