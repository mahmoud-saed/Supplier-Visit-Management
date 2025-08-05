{
    'name': 'Supplier Visit Management',
    'version': '1.0',
    'category': 'Purchase',
    'summary': 'Manage supplier visits with tracking and reporting',
    'description': """
        This module provides comprehensive supplier visit management functionality:
        - Create and track supplier visits
        - Auto-generate visit names using sequences
        - Integration with purchase orders
        - PDF reports and website pages
        - API integration for visit confirmations
        - Security and access control
    """,
    'author': 'Your Company',
    'website': 'https://www.yourcompany.com',
    'depends': [
        'base',
        'purchase',
        'website',
        'mail',
        'web',
    ],
    'data': [
        'security/supplier_visit_security.xml',
        'security/ir.model.access.csv',
        'data/supplier_visit_sequence.xml',
        'views/supplier_visit_views.xml',
        'views/res_partner_views.xml',
        'views/purchase_order_views.xml',
        'report/supplier_visit_report.xml',
        'report/supplier_visit_report_templates.xml',
        'wizard/supplier_visit_report_wizard.xml',
        'data/mail_template.xml',
        'views/website_templates.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'supplier_visit/static/src/js/supplier_visit_widget.js',
            'supplier_visit/static/src/xml/supplier_visit_widget.xml',
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
} 