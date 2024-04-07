#-*- coding: utf-8 -*-

from odoo import models, fields

class ManagedModel(models.Model):
    _name = 'managed.model'

    name = fields.Char('Name')
    description = fields.Text('Description')

