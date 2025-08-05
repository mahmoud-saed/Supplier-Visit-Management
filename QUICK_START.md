# Quick Start Guide - Supplier Visit Module

## 🚀 Run Locally with Docker (Easiest Method)

### Prerequisites
- Docker Desktop installed
- Docker Compose available

### Steps

1. **Install Docker Desktop**
   - Download from: https://www.docker.com/products/docker-desktop
   - Install and start Docker Desktop

2. **Start Odoo with the module**
   ```bash
   docker-compose up -d
   ```

3. **Access Odoo**
   - Open browser: http://localhost:8069
   - Create database or use existing one
   - Login with admin/admin

4. **Install the Supplier Visit Module**
   - Go to **Apps** menu
   - Click **Update Apps List**
   - Search for "Supplier Visit Management"
   - Click **Install**

5. **Test the Module**
   - Create a supplier (Contact with Vendor flag)
   - Go to **Supplier Visits** menu
   - Create a test visit
   - Test all features

## 🛑 Stop Odoo
```bash
docker-compose down
```

## 📋 Alternative Methods

### Method 2: Manual Installation
1. Install Odoo 16.0
2. Copy `supplier_visit` folder to addons directory
3. Update apps list and install module

### Method 3: Odoo.sh (Cloud)
1. Visit: https://www.odoo.sh
2. Create free trial account
3. Upload the `supplier_visit` module
4. Test in cloud environment

## 🔧 Troubleshooting

### Docker Issues
- Ensure Docker Desktop is running
- Check if port 8069 is available
- Try: `docker-compose down && docker-compose up -d`

### Module Not Found
- Verify `supplier_visit` folder is in the same directory as `docker-compose.yml`
- Check file permissions
- Update apps list in Odoo

### Database Issues
- Use default database: `postgres`
- Default credentials: admin/admin
- Create new database if needed

## 📱 Module Features to Test

1. **Create Supplier Visit**
   - Go to Supplier Visits menu
   - Click Create
   - Fill in details and save

2. **Test Purchase Order Integration**
   - Create purchase order with supplier
   - Confirm order
   - Check chatter for visit information

3. **Generate Reports**
   - Go to Reports menu
   - Select date range
   - Generate PDF report

4. **Test Website Page**
   - Visit: http://localhost:8069/supplier-visits
   - View supplier information

5. **Test API Integration**
   - Confirm a visit
   - Check chatter for API response

## 🎯 Success Indicators

- ✅ Module installs without errors
- ✅ Menu items appear correctly
- ✅ Can create supplier visits
- ✅ Sequence numbers generate automatically
- ✅ Purchase order integration works
- ✅ Reports generate correctly
- ✅ Website page is accessible
- ✅ API integration functions

## 📞 Support

If you encounter issues:
1. Check Docker logs: `docker-compose logs web`
2. Review the README.md file
3. Check test results in TEST_RESULTS.md
4. Verify all files are present in supplier_visit folder 