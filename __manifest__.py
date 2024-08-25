{
    'name': 'Estate',
    'version': '1.0',
    'depends':['base', 'mail'],
    'author': 'TomioDeCode',
    'category': 'App',
    'description': """ This is module is used to learn basic odoo 17 """,
    'application': True,
    'data': [
        # Security
        'security/ir.model.access.csv',
        
        # Views
        'views/estate_property.xml',
        'views/estate_property_type.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_tag.xml',
        'views/menu.xml',
        
        # Load initial Data
        'data/estate.property.csv',
        
        # Schedulers
        'views/schedulers/estate_property_scheduler.xml',
        
        # Template
        'data/templates/example_email_template.xml',
        
        # Report
        'views/reports/ouput_pdf/estate_property.xml'
    ]
}