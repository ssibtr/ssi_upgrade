# -*- coding: utf-8 -*-
from odoo import fields, models

class Employee(models.Model):
    _inherit = 'hr.employee'

    # Add a new column to the res.partner model, by default employee are not
    # commissionable
    is_commissionable = fields.Boolean(string="Commissionable", related="user_id.is_commissionable")
    