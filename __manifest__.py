{
    'name': "Appraisal",
    'version': '17.0.1.0.0',
    'category': 'Human Resources',
    'summary': """Roll out appraisal plans and get the best of your 
    workforce""",
    'description': """This app is a powerful and versatile tool that can help 
    organizations improve their employee appraisal process and boost employee 
    performance.""",
    'company': 'Tijus Academy',
    'depends': ['hr', 'survey'],
    'data': [
        'security/oh_appraisal_groups.xml',
        'security/hr_appraisal_security.xml',
        'security/ir.model.access.csv',
        'views/appraisal_templates.xml',
        'views/survey_user_input_views.xml',
        'views/hr_appraisal_views.xml',
        'views/menuitems.xml',
    ],
    'demo': [
        'data/hr_employee_demo.xml',
        'data/hr_appraisal_stages_demo.xml',
        'data/hr_appraisal_demo.xml'
    ],
    'license': "AGPL-3",
    'auto_install': False,
    'application': True,
}
