from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import requests
import logging

_logger = logging.getLogger(__name__)


class SupplierVisit(models.Model):
    _name = 'supplier.visit'
    _description = 'Supplier Visit'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'visit_date desc, id desc'

    name = fields.Char(
        string='Visit Reference',
        required=True,
        copy=False,
        readonly=True,
        default=lambda self: _('New')
    )
    
    supplier_id = fields.Many2one(
        'res.partner',
        string='Supplier',
        required=True,
        domain=[('supplier_rank', '>', 0)],
        tracking=True
    )
    
    visit_date = fields.Date(
        string='Visit Date',
        required=True,
        default=fields.Date.today,
        tracking=True
    )
    
    visitor_id = fields.Many2one(
        'res.users',
        string='Visitor',
        required=True,
        default=lambda self: self.env.user,
        tracking=True
    )
    
    notes = fields.Text(
        string='Notes',
        tracking=True
    )
    
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], string='Status', default='draft', tracking=True, required=True)
    
    # Computed fields
    supplier_name = fields.Char(
        string='Supplier Name',
        related='supplier_id.name',
        store=True
    )
    
    visitor_name = fields.Char(
        string='Visitor Name',
        related='visitor_id.name',
        store=True
    )

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('supplier.visit') or _('New')
        return super(SupplierVisit, self).create(vals)

    def action_confirm(self):
        """Confirm the visit and send API notification"""
        for visit in self:
            visit.state = 'confirmed'
            visit._send_api_notification()

    def action_done(self):
        """Mark visit as done"""
        self.state = 'done'

    def action_draft(self):
        """Reset to draft"""
        self.state = 'draft'

    def _send_api_notification(self):
        """Send POST request to external API when visit is confirmed"""
        try:
            payload = {
                'supplier_name': self.supplier_id.name,
                'visit_date': self.visit_date.strftime('%Y-%m-%d'),
                'user': self.visitor_id.name,
            }
            
            response = requests.post(
                'https://jsonplaceholder.typicode.com/posts',
                json=payload,
                timeout=10
            )
            
            if response.status_code == 201:
                self.message_post(
                    body=_('API notification sent successfully. Response: %s') % response.json().get('id', 'N/A')
                )
            else:
                self.message_post(
                    body=_('API notification failed. Status: %s') % response.status_code
                )
                
        except Exception as e:
            _logger.error('API notification failed: %s', str(e))
            self.message_post(
                body=_('API notification failed: %s') % str(e)
            )

    @api.constrains('visit_date')
    def _check_visit_date(self):
        """Ensure visit date is not in the future"""
        for record in self:
            if record.visit_date and record.visit_date > fields.Date.today():
                raise ValidationError(_('Visit date cannot be in the future.'))

    def get_visit_count(self, supplier_id, days=30):
        """Get visit count for a supplier in the last N days"""
        if not supplier_id:
            return 0
            
        from_date = fields.Date.today() - fields.timedelta(days=days)
        return self.search_count([
            ('supplier_id', '=', supplier_id),
            ('visit_date', '>=', from_date),
            ('state', 'in', ['confirmed', 'done'])
        ])

    def get_last_visit_date(self, supplier_id):
        """Get the last visit date for a supplier"""
        if not supplier_id:
            return False
            
        last_visit = self.search([
            ('supplier_id', '=', supplier_id),
            ('state', 'in', ['confirmed', 'done'])
        ], order='visit_date desc', limit=1)
        
        return last_visit.visit_date if last_visit else False 