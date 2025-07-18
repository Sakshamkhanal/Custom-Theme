{
    'name':'Website Airproof',
    'description':'A custom theme build on odoo 18',
    'category':'Theme',
    'version':'1.0',
    'author':'Saksham Khanal',
    'license':'LGPL-3',
    'installable':True,
    'depends':['website_sale','website_sale_wishlist'],
    'data':[
    'data/home.xml',
    'data/presets.xml',
    'data/images.xml',
    ],
    'assets':{
    'web._assets_primary_variables':[
        'website_airproof/static/src/scss/primary_variables.scss',
        ],
    'web._assets_frontend_helpers': [
      ('prepend', 'website_airproof/static/src/scss/bootstrap_overridden.scss'),
        ],
     },
}

