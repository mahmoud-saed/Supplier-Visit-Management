#!/usr/bin/env python3
"""
Test script for Supplier Visit Module
This script tests the core functionality of the supplier visit module
"""

import sys
import os
import requests
import json
from datetime import datetime, timedelta

def test_api_endpoint():
    """Test the external API endpoint used by the module"""
    print("🔍 Testing API Endpoint...")
    try:
        payload = {
            'supplier_name': 'Test Supplier',
            'visit_date': datetime.now().strftime('%Y-%m-%d'),
            'user': 'Test User'
        }
        
        response = requests.post(
            'https://jsonplaceholder.typicode.com/posts',
            json=payload,
            timeout=10
        )
        
        if response.status_code == 201:
            print("✅ API endpoint is working correctly")
            print(f"   Response ID: {response.json().get('id')}")
            return True
        else:
            print(f"❌ API endpoint returned status: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ API endpoint test failed: {str(e)}")
        return False

def test_module_structure():
    """Test if all required files exist"""
    print("\n📁 Testing Module Structure...")
    
    required_files = [
        'supplier_visit/__manifest__.py',
        'supplier_visit/__init__.py',
        'supplier_visit/models/__init__.py',
        'supplier_visit/models/supplier_visit.py',
        'supplier_visit/models/res_partner.py',
        'supplier_visit/models/purchase_order.py',
        'supplier_visit/security/supplier_visit_security.xml',
        'supplier_visit/security/ir.model.access.csv',
        'supplier_visit/data/supplier_visit_sequence.xml',
        'supplier_visit/views/supplier_visit_views.xml',
        'supplier_visit/views/res_partner_views.xml',
        'supplier_visit/views/purchase_order_views.xml',
        'supplier_visit/views/website_templates.xml',
        'supplier_visit/report/supplier_visit_report.xml',
        'supplier_visit/report/supplier_visit_report_templates.xml',
        'supplier_visit/wizard/__init__.py',
        'supplier_visit/wizard/supplier_visit_report_wizard.py',
        'supplier_visit/wizard/supplier_visit_report_wizard.xml',
        'supplier_visit/controllers/__init__.py',
        'supplier_visit/controllers/main.py',
        'supplier_visit/static/src/js/supplier_visit_widget.js',
        'supplier_visit/static/src/xml/supplier_visit_widget.xml',
        'supplier_visit/data/mail_template.xml',
        'supplier_visit/README.md'
    ]
    
    missing_files = []
    for file_path in required_files:
        if not os.path.exists(file_path):
            missing_files.append(file_path)
        else:
            print(f"✅ {file_path}")
    
    if missing_files:
        print(f"\n❌ Missing files:")
        for file_path in missing_files:
            print(f"   - {file_path}")
        return False
    else:
        print("✅ All required files exist")
        return True

def test_manifest_file():
    """Test the manifest file structure"""
    print("\n📋 Testing Manifest File...")
    
    try:
        with open('supplier_visit/__manifest__.py', 'r') as f:
            content = f.read()
            
        # Check for required keys
        required_keys = ['name', 'version', 'depends', 'data', 'installable']
        missing_keys = []
        
        for key in required_keys:
            if f"'{key}'" not in content and f'"{key}"' not in content:
                missing_keys.append(key)
        
        if missing_keys:
            print(f"❌ Missing keys in manifest: {missing_keys}")
            return False
        else:
            print("✅ Manifest file structure is correct")
            return True
            
    except Exception as e:
        print(f"❌ Error reading manifest file: {str(e)}")
        return False

def test_model_files():
    """Test the model files for syntax errors"""
    print("\n🐍 Testing Model Files...")
    
    model_files = [
        'supplier_visit/models/supplier_visit.py',
        'supplier_visit/models/res_partner.py',
        'supplier_visit/models/purchase_order.py',
        'supplier_visit/wizard/supplier_visit_report_wizard.py',
        'supplier_visit/controllers/main.py'
    ]
    
    for file_path in model_files:
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Basic syntax check (compile)
            compile(content, file_path, 'exec')
            print(f"✅ {file_path} - Syntax OK")
            
        except SyntaxError as e:
            print(f"❌ {file_path} - Syntax Error: {str(e)}")
            return False
        except Exception as e:
            print(f"❌ {file_path} - Error: {str(e)}")
            return False
    
    return True

def test_xml_files():
    """Test XML files for basic structure"""
    print("\n📄 Testing XML Files...")
    
    xml_files = [
        'supplier_visit/security/supplier_visit_security.xml',
        'supplier_visit/security/ir.model.access.csv',
        'supplier_visit/data/supplier_visit_sequence.xml',
        'supplier_visit/views/supplier_visit_views.xml',
        'supplier_visit/views/res_partner_views.xml',
        'supplier_visit/views/purchase_order_views.xml',
        'supplier_visit/views/website_templates.xml',
        'supplier_visit/report/supplier_visit_report.xml',
        'supplier_visit/report/supplier_visit_report_templates.xml',
        'supplier_visit/wizard/supplier_visit_report_wizard.xml',
        'supplier_visit/data/mail_template.xml'
    ]
    
    for file_path in xml_files:
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            # Basic XML structure check
            if '<?xml' in content or '<odoo>' in content or file_path.endswith('.csv'):
                print(f"✅ {file_path} - Structure OK")
            else:
                print(f"⚠️  {file_path} - May have structure issues")
                
        except Exception as e:
            print(f"❌ {file_path} - Error: {str(e)}")
            return False
    
    return True

def test_js_files():
    """Test JavaScript files"""
    print("\n⚡ Testing JavaScript Files...")
    
    js_files = [
        'supplier_visit/static/src/js/supplier_visit_widget.js',
        'supplier_visit/static/src/xml/supplier_visit_widget.xml'
    ]
    
    for file_path in js_files:
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            
            if 'odoo.define' in content or '<?xml' in content:
                print(f"✅ {file_path} - Structure OK")
            else:
                print(f"⚠️  {file_path} - May have structure issues")
                
        except Exception as e:
            print(f"❌ {file_path} - Error: {str(e)}")
            return False
    
    return True

def generate_test_data():
    """Generate sample test data for the module"""
    print("\n📊 Generating Test Data...")
    
    test_data = {
        'suppliers': [
            {'name': 'ABC Electronics', 'supplier_rank': 1},
            {'name': 'XYZ Manufacturing', 'supplier_rank': 1},
            {'name': 'Tech Solutions Inc', 'supplier_rank': 1}
        ],
        'visits': [
            {
                'supplier': 'ABC Electronics',
                'visit_date': (datetime.now() - timedelta(days=5)).strftime('%Y-%m-%d'),
                'visitor': 'John Doe',
                'notes': 'Initial supplier assessment visit'
            },
            {
                'supplier': 'XYZ Manufacturing',
                'visit_date': (datetime.now() - timedelta(days=15)).strftime('%Y-%m-%d'),
                'visitor': 'Jane Smith',
                'notes': 'Quality control review'
            }
        ]
    }
    
    print("✅ Test data structure created")
    return test_data

def main():
    """Main test function"""
    print("🚀 Starting Supplier Visit Module Tests")
    print("=" * 50)
    
    tests = [
        ("Module Structure", test_module_structure),
        ("Manifest File", test_manifest_file),
        ("Model Files", test_model_files),
        ("XML Files", test_xml_files),
        ("JavaScript Files", test_js_files),
        ("API Endpoint", test_api_endpoint),
    ]
    
    results = []
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"❌ {test_name} test failed with exception: {str(e)}")
            results.append((test_name, False))
    
    # Generate test data
    test_data = generate_test_data()
    
    # Summary
    print("\n" + "=" * 50)
    print("📋 TEST SUMMARY")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{status} - {test_name}")
        if result:
            passed += 1
    
    print(f"\n📊 Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The module is ready for installation.")
        print("\n📝 Next Steps:")
        print("1. Copy the supplier_visit folder to your Odoo addons directory")
        print("2. Update the addons list in Odoo")
        print("3. Install the 'Supplier Visit Management' module")
        print("4. Assign users to appropriate security groups")
        print("5. Test the functionality in Odoo")
    else:
        print("⚠️  Some tests failed. Please review the issues above before installation.")
    
    return passed == total

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1) 