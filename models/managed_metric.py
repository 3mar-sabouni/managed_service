#-*- coding: utf-8 -*-

from odoo import models, fields

class ManagedMetric(models.Model):
    _name = 'managed.metric'

    device_id = fields.Many2one('managed.device', 'Device', required=True)
    reading = fields.Integer('Reading', required=True)
    date = fields.Date('Date', required=True)
