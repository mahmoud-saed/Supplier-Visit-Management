# Supplier Visit Module - Installation Guide

## Prerequisites

- Odoo 16.0 or later
- Python 3.8+
- Required Odoo modules: `base`, `purchase`, `website`, `mail`, `web`
- Internet connection (for API testing)

## Installation Steps

### 1. Copy Module Files

```bash
# Copy the supplier_visit folder to your Odoo addons directory
cp -r supplier_visit /path/to/odoo/addons/
```

### 2. Update Addons List

1. Go to **Apps** in Odoo
2. Click **Update Apps List** (top-right corner)
3. Wait for the update to complete

### 3. Install the Module

1. Search for "Supplier Visit Management" in the Apps search
2. Click on the module
3. Click **Install** button
4. Wait for installation to complete

### 4. Configure Security Groups

1. Go to **Settings > Users & Companies > Users**
2. Select a user who should have access to supplier visits
3. In the **Access Rights** tab, add them to:
   - **Supplier Visit User** (for basic access)
   - **Supplier Visit Manager** (for full access including deletion)

### 5. Test the Module

#### Create a Test Supplier
1. Go to **Contacts**
2. Create a new contact
3. Set **Is a Company** = True
4. Set **Is a Vendor** = True
5. Save the contact

#### Create a Test Visit
1. Go to **Supplier Visits** (new menu)
2. Click **Create**
3. Fill in the details:
   - Supplier: Select your test supplier
   - Visit Date: Today's date
   - Visitor: Current user
   - Notes: "Test visit"
4. Save and click **Confirm**

#### Test Purchase Order Integration
1. Go to **Purchase > Purchase Orders**
2. Create a new purchase order
3. Select your test supplier
4. Add some products
5. Click **Confirm Order**
6. Check the chatter for visit information

#### Test Reports
1. Go to **Supplier Visits > Reports > Visit Summary Report**
2. Select date range
3. Click **Generate Report**

#### Test Website Page
1. Visit: `http://your-odoo-domain.com/supplier-visits`
2. Verify the page loads with supplier information

## Troubleshooting

### Common Issues

#### Module Not Found
- Ensure the module is in the correct addons directory
- Update the apps list
- Check file permissions

#### Import Errors
- Verify all Python files have correct syntax
- Check that all required dependencies are installed
- Review Odoo logs for specific error messages

#### Permission Errors
- Assign users to appropriate security groups
- Check access rights in `ir.model.access.csv`
- Verify record rules are correct

#### API Integration Issues
- Check internet connectivity
- Verify the API endpoint is accessible
- Review Odoo logs for API errors

### Log Files

Check these log locations for errors:
- Odoo server logs: `/var/log/odoo/odoo-server.log`
- Module-specific errors in Odoo interface: **Settings > Technical > Logging**

### Support

If you encounter issues:
1. Check the README.md file for detailed documentation
2. Review the test results from `test_supplier_visit.py`
3. Check Odoo community forums
4. Contact your system administrator

## Verification Checklist

- [ ] Module installs without errors
- [ ] Security groups are created
- [ ] Menu items appear correctly
- [ ] Can create supplier visits
- [ ] Sequence numbers are generated
- [ ] Purchase order integration works
- [ ] Reports generate correctly
- [ ] Website page is accessible
- [ ] API integration functions
- [ ] Kanban view displays properly
- [ ] Custom widget works in form view

## Performance Notes

- The module includes database indexes for optimal performance
- API calls are asynchronous to prevent blocking
- Reports use efficient queries with proper filtering
- Website pages include pagination for large datasets 