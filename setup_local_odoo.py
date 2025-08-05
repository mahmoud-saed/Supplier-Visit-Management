#!/usr/bin/env python3
"""
Setup script for local Odoo installation to test the supplier visit module
"""

import os
import sys
import subprocess
import platform

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ is required")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible")
    return True

def check_system():
    """Check operating system and provide installation instructions"""
    system = platform.system().lower()
    print(f"🔍 Detected system: {system}")
    
    if system == "windows":
        print("\n📋 For Windows, you have these options:")
        print("1. Use Docker (Recommended)")
        print("2. Install Odoo manually")
        print("3. Use Odoo.sh (Cloud)")
        
        print("\n🚀 Quick Docker Setup:")
        print("1. Install Docker Desktop from https://www.docker.com/products/docker-desktop")
        print("2. Run: docker run -d -p 8069:8069 --name odoo odoo:16.0")
        print("3. Access Odoo at: http://localhost:8069")
        
    elif system == "linux":
        print("\n📋 For Linux (Ubuntu/Debian):")
        print("1. Install dependencies:")
        print("   sudo apt update")
        print("   sudo apt install python3-pip postgresql postgresql-client")
        print("2. Install Odoo:")
        print("   pip3 install odoo")
        print("3. Create database and run Odoo")
        
    elif system == "darwin":  # macOS
        print("\n📋 For macOS:")
        print("1. Install Homebrew if not installed:")
        print("   /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
        print("2. Install dependencies:")
        print("   brew install postgresql")
        print("   brew install python3")
        print("3. Install Odoo:")
        print("   pip3 install odoo")
    
    return system

def create_docker_compose():
    """Create a docker-compose.yml file for easy Odoo setup"""
    docker_compose_content = """version: '3.1'
services:
  web:
    image: odoo:16.0
    depends_on:
      - db
    ports:
      - "8069:8069"
    volumes:
      - odoo-web-data:/var/lib/odoo
      - ./supplier_visit:/mnt/extra-addons/supplier_visit
    environment:
      - HOST=db
      - USER=odoo
      - PASSWORD=odoo
    command: -- --dev=reload

  db:
    image: postgres:13
    environment:
      - POSTGRES_DB=postgres
      - POSTGRES_PASSWORD=odoo
      - POSTGRES_USER=odoo
    volumes:
      - odoo-db-data:/var/lib/postgresql/data

volumes:
  odoo-web-data:
  odoo-db-data:
"""
    
    with open('docker-compose.yml', 'w') as f:
        f.write(docker_compose_content)
    
    print("✅ Created docker-compose.yml file")
    print("📝 To start Odoo with the supplier visit module:")
    print("   docker-compose up -d")
    print("   Access Odoo at: http://localhost:8069")

def create_installation_script():
    """Create a simple installation script"""
    script_content = """#!/bin/bash
# Quick Odoo Installation Script

echo "🚀 Setting up Odoo for supplier visit module testing..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    echo "   Visit: https://www.docker.com/products/docker-desktop"
    exit 1
fi

# Check if docker-compose is available
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are available"

# Start Odoo with the supplier visit module
echo "🔧 Starting Odoo with supplier visit module..."
docker-compose up -d

echo "⏳ Waiting for Odoo to start..."
sleep 10

echo "🎉 Odoo is now running!"
echo "📱 Access Odoo at: http://localhost:8069"
echo "📋 Default credentials:"
echo "   Database: postgres"
echo "   Email: admin"
echo "   Password: admin"
echo ""
echo "📝 To install the supplier visit module:"
echo "1. Go to Apps menu"
echo "2. Update Apps List"
echo "3. Search for 'Supplier Visit Management'"
echo "4. Click Install"
echo ""
echo "🛑 To stop Odoo: docker-compose down"
"""
    
    with open('start_odoo.sh', 'w') as f:
        f.write(script_content)
    
    # Make it executable on Unix systems
    if platform.system().lower() != "windows":
        os.chmod('start_odoo.sh', 0o755)
    
    print("✅ Created start_odoo.sh script")

def main():
    """Main setup function"""
    print("🚀 Odoo Local Setup for Supplier Visit Module")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        return
    
    # Check system and provide instructions
    system = check_system()
    
    print("\n" + "=" * 50)
    print("📋 SETUP OPTIONS")
    print("=" * 50)
    
    # Create Docker Compose file
    create_docker_compose()
    
    # Create installation script
    create_installation_script()
    
    print("\n" + "=" * 50)
    print("🎯 RECOMMENDED APPROACH")
    print("=" * 50)
    
    if system == "windows":
        print("1. Install Docker Desktop")
        print("2. Run: docker-compose up -d")
        print("3. Access: http://localhost:8069")
        print("4. Install the supplier visit module")
    else:
        print("1. Run: ./start_odoo.sh")
        print("2. Access: http://localhost:8069")
        print("3. Install the supplier visit module")
    
    print("\n📚 Alternative: Use Odoo.sh")
    print("- Visit: https://www.odoo.sh")
    print("- Create a free trial account")
    print("- Upload the supplier_visit module")
    print("- Test in the cloud environment")
    
    print("\n✅ Setup files created!")
    print("📁 Files created:")
    print("   - docker-compose.yml")
    print("   - start_odoo.sh")
    print("   - supplier_visit/ (your module)")

if __name__ == "__main__":
    main() 