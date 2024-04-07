from odoo import models, fields, api

class HelpdeskTicketExtension(models.Model):
    _inherit = 'helpdesk.ticket'

    device_id = fields.Many2one('managed.device', 'Device')
    serial_number = fields.Char('Serial Number', related='device_id.serial_number', readonly=True, store=True)
