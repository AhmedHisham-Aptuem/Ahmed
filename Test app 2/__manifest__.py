#############################################################################
#
#    Aptuem solutions.
#
#    Copyright (C) 2025-TODAY Aptuem solutions(<https://aptuem.com>)
#    Author: Ahmed Hisham (<https://aptuem.com>)
#
#    You can't modify this app under any circumstances.
#
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    "name": "Ahmed app",

    'version': "18.0",
    
    'price': "1000 USD",
    
    'category': "Sales",

    'summary': "This app adds a fild on Sales order. Keywords: App, add, field, sales, order,.",

    'description': """
    This is the description of the app that adds a field on the sales order.

    Key Features:
    - This is the key features of the app that adds a field on the sales order.

    Benefits:
    - This is the benefits of the app that adds a field on the sales order.
""",


    'author': 'Ahmed',

    'website': "https://www.aptuem.com",

    "depends": ['sales'],

    "data": [
        "views/res_users_view.xml",
        "security/security.xml",
    ],

    'images': ['static/description/banner.svg'],
    'license': "OPL-1",
    'installable': True,
    'application': True,
    'auto_install': False,
}
