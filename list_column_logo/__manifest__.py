{
    'name': 'List Column Logo',
    'summary': 'Adds a list widget "column_logo" and a logo field on ir.model.fields',
    'version': '18.0.1.0.0',
    'author': 'Nguyen Ho',
    'category': 'Tools',
    'depends': ['base', 'web'],
    'data': [
        'views/actions.xml',
        'views/ir_model_fields_views.xml',
        'views/ir_model_field_logo_views.xml',
        'security/ir.model.access.csv',
    ],
    'assets': {
        'web.assets_backend': [
            'list_column_logo/static/src/js/list_logo_patch.js',
            ('after', 'web/static/src/views/list/list_renderer.xml', 'list_column_logo/static/src/xml/list_logo_templates.xml'),
            'list_column_logo/static/src/scss/list_logo.scss',
        ],
    },
    'images': ['static/description/icon.png'],
    'license': 'OPL-1',
    'support': 'nguyenhk277@gmail.com',
    'price': 9.99,
    'currency': 'USD',
    'installable': True,
    'application': False,
}
