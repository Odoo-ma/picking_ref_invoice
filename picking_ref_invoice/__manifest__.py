# -*- coding: utf-8 -*-
{
    'name': "Reference bons de livraison dans la facture",

    'summary': 'Reference bons de livraison dans la facture',

    'description': """
        Ce module Odoo permet de afficher la reference des bons de livraison sur la facture,
        facturation marocaine, Maroc
        """,

    'author': "M B",
    'license': "AGPL-3",
    'category': 'Invoicing',
    'version': '16.0',
    "depends": ["stock", "account"],
    'images': ['static/description/icon.png'],
    'images': ['static/description/cover.png'],
    "data": [
        'views/account_move_views.xml',
        'reports/invoice_report.xml',
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
}



