{
    "name": "Warehouse Restriction",

    'version': "18.0",

    'category': "Stock",

    'summary': "Restrict user access to specific warehouses in Odoo. Enhance inventory control and data security by limiting warehouse visibility and operations based on user roles. Keywords: Warehouse Restriction, Odoo Warehouse Management, User Access Control, Inventory Security, Warehouse Access Limitations, Odoo Inventory Restriction, Role-Based Access Control, Warehouse Permissions.",

    'description': """
    The eg_warehouse_restriction module allows warehouse managers to control access to specific warehouses for individual users. 
    By restricting access, this app helps ensure that only authorized personnel can view, edit, or manage certain warehouse operations, 
    enhancing security and improving workflow management.

    Key Features:
    - User Access Control: Restrict specific users from accessing particular warehouses within your Odoo system.
    - Customizable Permissions: Define and manage which users have access to which warehouses, providing fine-grained control over warehouse data.
    - Improved Security: Prevent unauthorized users from performing critical warehouse operations, ensuring sensitive information and stock management are kept secure.
    - Seamless Integration: Fully integrates with Odoo’s warehouse and inventory modules.

    Benefits:
    - Enhanced Security: Limit access to sensitive warehouse data, reducing the risk of unauthorized transactions.
    - Better Workflow Management: Maintain clear distinctions between users’ roles and responsibilities within warehouse operations.
    - Easy Configuration: Set up user restrictions with a simple and user-friendly interface.
""",


    'author': 'INKERP',

    'website': "https://www.inkerp.com",

    "depends": ['stock'],

    "data": [
        "views/res_users_view.xml",
        "security/security.xml",
    ],

    'images': ['static/description/banner.png'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
