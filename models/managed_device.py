#-*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ManagedDevice(models.Model):
    _name = 'managed.device'

    serial_number = fields.Char('Serial Number', required=True)

    # Unique constraint for serial number
    _sql_constraints = [
        ('unique_serial_number', 'UNIQUE(serial_number)', 'Serial number must be unique.')
    ]

    @api.constrains('serial_number')
    def _check_serial_number_length(self):
        for record in self:
            if len(record.serial_number) > 25:
                raise ValidationError("Serial number must be at most 25 characters long.")

    model_id = fields.Many2one('managed.model', 'Model', required=True)
    type = fields.Many2one('device.type', 'Type', required=True)
    owner = fields.Many2one('res.partner', 'Owner')
    installation_date = fields.Date('Installation Date')
    pm_cycle = fields.Integer('PM Cycle', required=True)
    pm_unit = fields.Selection([('hours', 'Hours'), ('days', 'Days'), ('pages', 'Pages')], 'PM Unit', required=True)
    last_pm_counter = fields.Integer('Last PM Counter')


class DeviceType(models.Model):
    _name = 'device.type'
    _description = 'Device Type'

    name = fields.Char('Name', required=True)