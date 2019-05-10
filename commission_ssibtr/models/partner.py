# -*- coding: utf-8 -*-
from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.users'

    # Add a new column to the res.partner model, by default partners are not
    # commissionable
    is_commissionable = fields.Boolean(string="Commissionable", default=False)
    