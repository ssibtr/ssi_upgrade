# -*- coding: utf-8 -*-
from odoo import fields, models

class Timesheet(models.Model):
    _inherit = 'account.analytic.line'

    task_id = fields.Many2one('project.task',"Taskzp", domain=[('stage_id.name','not ilike','complete')])
