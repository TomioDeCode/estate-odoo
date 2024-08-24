{
    'name': 'Estate',
    'version': '1.0',
    'depends':['base', 'mail'],
    'author': 'TomioDeCode',
    'category': 'App',
    'description': """ This is module is used to learn basic odoo 17 """,
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/estate_property.xml',
        
        # Load initial Data
        'data/estate.property.csv',
        
        # Schedulers
        'views/schedulers/estate_property_scheduler.xml',
        
        # Template
        'data/templates/example_email_template.xml'
    ]
}