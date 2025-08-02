#!/usr/bin/env python3
"""
Quick Start Script for Student Management System

This script helps you get the Student Management System up and running quickly.
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"\n{description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} completed successfully!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed!")
        print(f"Error: {e.stderr}")
        return False

def check_python_version():
    """Check if Python version is compatible"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 7):
        print("❌ Python 3.7 or higher is required!")
        print(f"Current version: {version.major}.{version.minor}.{version.micro}")
        return False
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} is compatible!")
    return True

def main():
    """Main quick start function"""
    print("=== Student Management System - Quick Start ===\n")
    
    # Check Python version
    if not check_python_version():
        return
    
    # Check if requirements.txt exists
    if not os.path.exists('requirements.txt'):
        print("❌ requirements.txt not found! Make sure you're in the correct directory.")
        return
    
    # Install dependencies
    print("\n📦 Installing Python dependencies...")
    if not run_command("pip install -r requirements.txt", "Installing dependencies"):
        print("\n💡 Try running: pip install -r requirements.txt manually")
        return
    
    # Check if MySQL is available
    print("\n🔍 Checking MySQL connection...")
    try:
        import mysql.connector
        print("✅ MySQL connector is available!")
    except ImportError:
        print("❌ MySQL connector not installed!")
        return
    
    # Run database setup
    print("\n🗄️ Setting up database...")
    if os.path.exists('setup_database.py'):
        if not run_command("python setup_database.py", "Database setup"):
            print("\n💡 You can run the database setup manually:")
            print("python setup_database.py")
            return
    else:
        print("⚠️ setup_database.py not found. You may need to set up the database manually.")
    
    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Make sure MySQL server is running")
    print("2. Run the application: python app.py")
    print("3. Open your browser and go to: http://localhost:5000")
    print("\n📚 For more information, see README.md")

if __name__ == "__main__":
    main() 