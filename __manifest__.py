{
    'name': "Joining Form",
    'version': "14.0.1.0",
    'sequence': "0",
    'depends': ['base', 'website', 'hr', 'mail'],
    'data': [
        'data/activity.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/web_form_view.xml',
        'views/employee_datas.xml',
        'views/employee_form_module.xml',
        'views/link_employee.xml',

    ],
    'demo': [],
    'summary': "logic_employee_form",
    'description': "this_is_my_app",
    'installable': True,
    'auto_install': False,
    'license': "LGPL-3",
    'application': False
}
