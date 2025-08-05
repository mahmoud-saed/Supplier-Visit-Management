from odoo import models, api, _
from odoo.exceptions import UserError


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def button_confirm(self):
        """Override to check supplier visits before confirmation"""
        for order in self:
            if order.partner_id.supplier_rank > 0:
                self._check_supplier_visits(order.partner_id)
        
        return super(PurchaseOrder, self).button_confirm()

    def _check_supplier_visits(self, supplier):
        """Check if supplier has visits in the last 30 days"""
        visit_count = self.env['supplier.visit'].get_visit_count(supplier.id, days=30)
        last_visit_date = self.env['supplier.visit'].get_last_visit_date(supplier.id)
        
        if visit_count == 0:
            # No visits in last 30 days - log warning
            self.message_post(
                body=_('WARNING: No supplier visits found for %s in the last 30 days.') % supplier.name
            )
        else:
            # Visits found - log note with last visit date
            if last_visit_date:
                self.message_post(
                    body=_('INFO: Supplier visit information: Last visit to %s was on %s.') % (
                        supplier.name, last_visit_date.strftime('%Y-%m-%d')
                    )
                ) 