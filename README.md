# Supplier Visit Management

A comprehensive Odoo module for managing supplier visits with tracking, reporting, and integration capabilities.

## 🚀 Quick Start

### Option 1: Docker (Recommended)
```bash
# Clone the repository
git clone https://github.com/mahmoud-saed/Supplier-Visit-Management.git
cd Supplier-Visit-Management

# Start Odoo with the module
docker-compose up -d

# Access Odoo at: http://localhost:8069
```

### Option 2: Manual Installation
1. Copy the `supplier_visit` folder to your Odoo addons directory
2. Update the addons list in Odoo
3. Install the "Supplier Visit Management" module

## 📋 Features

- **Supplier Visit Tracking**: Create and manage supplier visits with auto-generated sequences
- **Purchase Order Integration**: Automatic visit checking when confirming purchase orders
- **PDF Reports**: Generate comprehensive visit summary reports
- **Public Website**: Public access to supplier visit information
- **API Integration**: External API notifications on visit confirmation
- **Security Groups**: Role-based access control
- **Email Templates**: Automated notifications

## 📁 Project Structure

```
Supplier Visit Management/
├── README.md                    # This file - Project overview
├── INSTALLATION_GUIDE.md        # Detailed installation instructions
├── QUICK_START.md              # Quick start guide
├── TEST_RESULTS.md             # Test documentation
├── docker-compose.yml          # Docker configuration
├── setup_local_odoo.py         # Setup script
├── test_supplier_visit.py      # Test files
├── .gitignore                  # Git ignore rules
└── supplier_visit/             # The Odoo module
    ├── README.md               # Module-specific documentation
    ├── __manifest__.py         # Module manifest
    ├── models/                 # Python models
    ├── views/                  # XML views
    ├── security/               # Security rules
    ├── data/                   # Data files
    ├── report/                 # Report templates
    ├── wizard/                 # Wizard models
    ├── controllers/            # Web controllers
    └── static/                 # Static assets
```

## 🛠️ Requirements

- Odoo 16.0 or later
- Python 3.8+
- Required Odoo modules: `base`, `purchase`, `website`, `mail`, `web`

## 📖 Documentation

- **[Installation Guide](INSTALLATION_GUIDE.md)** - Detailed setup instructions
- **[Quick Start Guide](QUICK_START.md)** - Get up and running quickly
- **[Test Results](TEST_RESULTS.md)** - Test documentation and results
- **[Module Documentation](supplier_visit/README.md)** - Detailed module features

## 🧪 Testing

Run the test suite:
```bash
python test_supplier_visit.py
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is licensed under the LGPL-3 License.

## 🆘 Support

For issues and questions:
1. Check the [Installation Guide](INSTALLATION_GUIDE.md)
2. Review the [Test Results](TEST_RESULTS.md)
3. Open an issue on GitHub

## 🔗 Links

- **Repository**: https://github.com/mahmoud-saed/Supplier-Visit-Management
- **Odoo**: https://www.odoo.com
- **Documentation**: See the docs folder for detailed guides
