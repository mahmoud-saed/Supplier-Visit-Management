# Supplier Visit Management Module

A comprehensive Odoo module for managing supplier visits with tracking, reporting, and integration capabilities.

## Features

### 1. Core Supplier Visit Management
- **Model**: `supplier.visit`
- **Fields**:
  - `name`: Auto-generated sequence (VISIT/YYYY/XXXXX)
  - `supplier_id`: Many2one to res.partner (suppliers only)
  - `visit_date`: Date field
  - `visitor_id`: Many2one to res.users
  - `notes`: Text field for visit details
  - `state`: Selection (draft, confirmed, done)

### 2. Security & Access Control
- Custom security groups:
  - **Supplier Visit User**: Can create and view visits
  - **Supplier Visit Manager**: Full access including deletion
- Proper access rights defined in `ir.model.access.csv`
- Multi-company support

### 3. Integration with Purchase Module
- Smart button in supplier form to view related visits
- Purchase order confirmation triggers visit checking:
  - Warns if no visits in last 30 days
  - Shows last visit date if visits exist
- Visit count and last visit date displayed in supplier form

### 4. QWeb PDF Report
- **Report Name**: "Supplier Visit Summary"
- **Features**:
  - Date range filtering
  - Optional supplier filtering
  - Professional PDF layout
  - Visit details with status indicators

### 5. Public Website Page
- **Route**: `/supplier-visits`
- **Features**:
  - Public access to supplier visit information
  - Pagination (20 records per page)
  - Last visit date display
  - Visit count statistics
  - Responsive design

### 6. API Integration
- **Trigger**: Visit confirmation
- **Endpoint**: `https://jsonplaceholder.typicode.com/posts`
- **Payload**: supplier_name, visit_date, user
- **Response**: Logged in visit chatter

### 7. Bonus Features
- **Kanban View**: Color-coded by state (draft=gray, confirmed=blue, done=green)
- **Custom JS Widget**: Mock supplier rating (1-5 stars) with random generation
- **Email Templates**: Automated notifications for visit confirmations

## Installation

1. Copy the `supplier_visit` folder to your Odoo addons directory
2. Update the addons list in Odoo
3. Install the "Supplier Visit Management" module
4. Assign users to appropriate security groups

## Usage

### Creating a Supplier Visit
1. Navigate to **Supplier Visits** menu
2. Click **Create** button
3. Select supplier, date, visitor, and add notes
4. Save and confirm the visit

### Generating Reports
1. Go to **Supplier Visits > Reports > Visit Summary Report**
2. Select date range and optional supplier
3. Click **Generate Report**

### Viewing Public Information
- Visit `/supplier-visits` on your website
- View supplier visit statistics and last visit dates

### Purchase Order Integration
- When confirming a purchase order, the system automatically checks supplier visit history
- Warnings and information are logged in the purchase order chatter

## Technical Details

### Dependencies
- `base`
- `purchase`
- `website`
- `mail`
- `web`

### Key Models
- `supplier.visit`: Main visit model
- `res.partner`: Extended with visit information
- `purchase.order`: Extended with visit checking
- `supplier.visit.report.wizard`: Report filtering

### Security Groups
- `group_supplier_visit_user`: Basic access
- `group_supplier_visit_manager`: Full access

### API Integration
The module sends POST requests to external APIs when visits are confirmed. The payload includes:
```json
{
    "supplier_name": "Supplier Name",
    "visit_date": "2024-01-15",
    "user": "Visitor Name"
}
```

## Customization

### Adding New Fields
To add new fields to the supplier visit model, modify `models/supplier_visit.py` and update the corresponding views.

### Modifying API Endpoint
Change the API URL in the `_send_api_notification` method in `models/supplier_visit.py`.

### Customizing Reports
Modify the QWeb templates in `report/supplier_visit_report_templates.xml` to customize the PDF report layout.

## Troubleshooting

### Common Issues
1. **Sequence not working**: Ensure the sequence data is properly loaded
2. **API calls failing**: Check network connectivity and API endpoint availability
3. **Security access denied**: Verify user is assigned to appropriate security groups

### Logs
Check Odoo logs for API integration errors and visit-related activities.

## Support

For issues and questions, please refer to the module documentation or contact your system administrator. 