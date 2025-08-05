from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    supplier_visit_count = fields.Integer(
        string='Visit Count',
        compute='_compute_supplier_visit_count'
    )
    
    last_visit_date = fields.Date(
        string='Last Visit Date',
        compute='_compute_last_visit_date'
    )

    @api.depends('supplier_rank')
    def _compute_supplier_visit_count(self):
        """Compute the number of visits for this supplier"""
        for partner in self:
            if partner.supplier_rank > 0:
                partner.supplier_visit_count = self.env['supplier.visit'].search_count([
                    ('supplier_id', '=', partner.id)
                ])
            else:
                partner.supplier_visit_count = 0

    @api.depends('supplier_rank')
    def _compute_last_visit_date(self):
        """Compute the last visit date for this supplier"""
        for partner in self:
            if partner.supplier_rank > 0:
                partner.last_visit_date = self.env['supplier.visit'].get_last_visit_date(partner.id)
            else:
                partner.last_visit_date = False

    def action_view_supplier_visits(self):
        """Smart button action to view supplier visits"""
        self.ensure_one()
        action = self.env['ir.actions.actions']._for_xml_id('supplier_visit.action_supplier_visit')
        action['domain'] = [('supplier_id', '=', self.id)]
        action['context'] = {
            'default_supplier_id': self.id,
            'search_default_supplier_id': self.id,
        }
        return action 