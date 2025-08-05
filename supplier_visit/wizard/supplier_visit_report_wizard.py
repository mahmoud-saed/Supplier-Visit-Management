from odoo import models, fields, api


class SupplierVisitReportWizard(models.TransientModel):
    _name = 'supplier.visit.report.wizard'
    _description = 'Supplier Visit Report Wizard'

    date_from = fields.Date(
        string='Date From',
        required=True,
        default=fields.Date.today
    )
    
    date_to = fields.Date(
        string='Date To',
        required=True,
        default=fields.Date.today
    )
    
    supplier_id = fields.Many2one(
        'res.partner',
        string='Supplier',
        domain=[('supplier_rank', '>', 0)]
    )

    def action_generate_report(self):
        """Generate the supplier visit report"""
        data = {
            'date_from': self.date_from,
            'date_to': self.date_to,
            'supplier_id': self.supplier_id.id if self.supplier_id else False,
            'supplier_name': self.supplier_id.name if self.supplier_id else 'All Suppliers',
        }
        
        return self.env.ref('supplier_visit.action_supplier_visit_summary_report').report_action(self, data=data) 