from odoo import http
from odoo.http import request
import math


class SupplierVisitController(http.Controller):

    @http.route('/supplier-visits', type='http', auth='public', website=True)
    def supplier_visits_page(self, **kwargs):
        """Public page listing suppliers with their last visit date"""
        
        # Get pagination parameters
        page = int(kwargs.get('page', 1))
        per_page = 20
        
        # Get suppliers with visit information
        suppliers = request.env['res.partner'].search([
            ('supplier_rank', '>', 0),
            ('is_company', '=', True)
        ], order='name')
        
        # Calculate pagination
        total_suppliers = len(suppliers)
        total_pages = math.ceil(total_suppliers / per_page)
        
        # Get suppliers for current page
        start = (page - 1) * per_page
        end = start + per_page
        page_suppliers = suppliers[start:end]
        
        # Get visit data for suppliers
        supplier_data = []
        for supplier in page_suppliers:
            last_visit_date = request.env['supplier.visit'].get_last_visit_date(supplier.id)
            visit_count = request.env['supplier.visit'].search_count([
                ('supplier_id', '=', supplier.id)
            ])
            
            supplier_data.append({
                'supplier': supplier,
                'last_visit_date': last_visit_date,
                'visit_count': visit_count,
            })
        
        values = {
            'suppliers': supplier_data,
            'pagination': {
                'page': page,
                'total_pages': total_pages,
                'total_suppliers': total_suppliers,
                'per_page': per_page,
                'has_prev': page > 1,
                'has_next': page < total_pages,
                'prev_page': page - 1,
                'next_page': page + 1,
            }
        }
        
        return request.render('supplier_visit.supplier_visits_page', values) 