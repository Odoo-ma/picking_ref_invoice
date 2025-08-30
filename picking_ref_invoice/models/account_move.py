from odoo import models, fields, api

class AccountMoveLine(models.Model):
    _inherit = 'account.move.line'

    picking_names = fields.Char(
        string='Bon de livraison',
        compute='_compute_picking_names',
        store=False
    )


    picking_date = fields.Date(
        string="Date BL",
        compute="_compute_picking_date",
        store=False
    )

    def _compute_picking_date(self):
        for line in self:
            if line.picking_names:
                # récupérer le(s) picking(s) directement par leur nom
                pickings = self.env['stock.picking'].search([('name', 'in', line.picking_names.split(', '))], limit=1)
                line.picking_date = pickings.date_done.date() if pickings and pickings.date_done else False
            else:
                line.picking_date = False
############################""
    def _compute_picking_names(self):
        for line in self:
            pickings = line.sale_line_ids.mapped('order_id.picking_ids').filtered(
                lambda p: p.state not in ('cancel') and p.picking_type_id.code == 'outgoing'
            )
            line.picking_names = ', '.join(pickings.mapped('name'))
