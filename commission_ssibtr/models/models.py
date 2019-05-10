# -*- coding: utf-8 -*-

from odoo import models, fields, api, exceptions
from datetime import datetime


class Commission(models.Model):
    _name = 'sale.commission'

    _inherit = [
        'mail.thread',
    ]

    #Main
    name = fields.Char(string="Title")
    sale_order = fields.Many2one('sale.order', 
        ondelete='set null', string="Sale Order", index=True)
    order_lines = fields.One2many(string='Order Lines', related="sale_order.order_line", inverse_name="commission_id")
    partner_id = fields.Many2one('res.partner',
         ondelete='set null', string="Customer", index=True)
    sales_person = fields.Many2one('res.users',
         ondelete='set null', string="Sales Person", index=True)
    status =  fields.Selection(string="Status", selection=[
            ('ncommissionable', 'Not Commissionable'),
            ('pending', 'Pending Manager Review'),
            ('eligible', 'Commissionable Sale'),
            ('approved', 'Approved / Ready for Payment'),
            ('paid', 'Paid'),
        ], default='pending', track_visibility='onchange')

    #Dates
    close_month = fields.Date(string="Close Month")
    #***Populate when status change to approved***
    approval_date = fields.Date(string="Approval Date", readonly=True)
    #***Manual Entries*** 
    pay_date = fields.Date(string="Pay Date")
   
    #Prices
    hardware_total = fields.Float(string="Hardware Total")
    hardware_factor = fields.Float(string="hardware_factor", default=1.00)
    hardware_percent = fields.Float(string="hardware_percent", default=0)
    hardware_commission = fields.Float(string="hardware_commission", compute="hwcommission")

    software_total = fields.Float(string="Software Total")
    software_factor = fields.Float(string="software_factor", default=1.00)
    software_percent = fields.Float(string="software_percent", default=0)
    software_commission = fields.Float(string="software_commission", compute="swcommission")

    labor_total = fields.Float(string="Labor Total")
    labor_factor = fields.Float(string="labor_factor", default=1.00)
    labor_percent = fields.Float(string="labor_percent", default=0)
    labor_commission = fields.Float(string="labor_commission", compute="lbcommission")

    commission_total = fields.Float(string="Commission Total")
    commission_subtotal_total = fields.Float(string="commission_subtotal_total", compute="ccommission")
    # commission_percent = fields.Float(string="commission_percent", default=0)
  
      
    commission_percent =  fields.Selection(string="Commission Percent", selection=[
        ('0', '0%'),
        ('5', '5%'),
        ('6.5', '6.5%'),
        ('8', '8%'),
        ('9.5', '9.5%'),
        ('100', '100%'),
    ], default='0')
  
    final_commission = fields.Float(string="Commission", compute="fcommission",  track_visibility='onchange')

    #Methods
    @api.depends('hardware_total', 'hardware_factor', 'hardware_percent')
    def hwcommission(self):
        for r in self:
            r.hardware_commission = r.hardware_total * r.hardware_factor
            r.hardware_commission = (r.hardware_percent * r.hardware_commission) / 100.0

    @api.depends('software_total', 'software_factor', 'software_percent')
    def swcommission(self):
        for r in self:
            r.software_commission = r.software_total * r.software_factor
            r.software_commission = (r.software_percent * r.software_commission) / 100.0

    @api.depends('labor_total', 'labor_factor', 'labor_percent')
    def lbcommission(self):
        for r in self:
            r.labor_commission = r.labor_total * r.labor_factor
            r.labor_commission = (r.labor_percent * r.labor_commission) / 100.0


    @api.depends('hardware_commission', 'software_commission', 'labor_commission')
    def ccommission(self):
        for r in self:
            r.commission_subtotal_total = r.hardware_commission + r.software_commission + r.labor_commission

    @api.depends('commission_subtotal_total', 'commission_percent')
    def fcommission(self):
        for r in self:
            r.final_commission = float(float(r.commission_percent) * float(r.commission_subtotal_total)) / 100.00

    @api.one
    def action_ncommissionable(self):
        self.write({
            'status': 'ncommissionable',
        })
    
    @api.one
    def action_pending(self):
        self.write({
            'status': 'pending',
        })

    @api.one
    def action_eligible(self):
        self.write({
            'status': 'eligible',
        })
    
    @api.one
    def action_approved(self):
        self.approval_date = datetime.today()
        self.write({
            'status': 'approved',
        })

    @api.one
    def action_paid(self):
        self.write({
            'status': 'paid',
        })



        