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

from odoo import fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    warehouse_ids = fields.Many2many(comodel_name='stock.warehouse', string='Warehouse')
