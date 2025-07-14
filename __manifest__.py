{
    'name':'Custom Theme',
    'description':'A custom theme build on odoo 18',
    'category':'Theme',
    'version':'1.0',
    'author':'Saksham Khanal',
    'license':'LGPL-3',
    'depends':['website'],
    'installable':True,

    'assets':{
    'web._assets_primary_variable':[
        'custom_addons18/scss/primary_variables.scss',
        ],
     },
}
