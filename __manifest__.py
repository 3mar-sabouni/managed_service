# -*- coding: utf-8 -*-
{
    'name': "Managed Service",
    'summary': " A new app called 'Managed Service' and integrate it with the existing Help Desk App",
    'description': """
    """,
    'author': "Omar Sabouni",
    'website': "",
    'category': 'Helpdesk',
    'version': '0.1',
    'depends': ['base','contacts','helpdesk'],
    'data': [
         'security/ir.model.access.csv',
         'views/managed_model_views.xml',
         'views/managed_device_views.xml',
         'views/device_type_views.xml',
         'views/managed_metric_views.xml',
         'views/helpdesk_ticket_inherit.xml',
         'data/ir.sequenc.xml'
         
    ],
    'demo': [
        #  'demo/demo.xml',
    ],
}

