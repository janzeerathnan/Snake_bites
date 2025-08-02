#!/usr/bin/env python3
"""
Database Setup Script for Student Management System

This script helps you set up the MySQL database for the Student Management System.
It will create the database and tables if they don't exist.
"""

import mysql.connector
from mysql.connector import Error
import getpass

def setup_database():
    """Set up the database and tables"""
    
    print("=== Student Management System - Database Setup ===\n")
    
    # Get database configuration from user
    print("Please provide your MySQL database credentials:")
    host = input("Host (default: localhost): ").strip() or "localhost"
    user = input("Username (default: root): ").strip() or "root"
    password = getpass.getpass("Password (leave empty if none): ").strip()
    
    # Test connection without specifying database
    config = {
        'host': host,
        'user': user,
        'password': password
    }
    
    try:
        print("\nTesting connection to MySQL server...")
        connection = mysql.connector.connect(**config)
        
        if connection.is_connected():
            print("✅ Successfully connected to MySQL server!")
            
            cursor = connection.cursor()
            
            # Create database
            print("\nCreating database 'student_db'...")
            cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
            print("✅ Database 'student_db' created/verified!")
            
            # Use the database
            cursor.execute("USE student_db")
            
            # Create students table
            print("\nCreating 'students' table...")
            create_table_query = """
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL UNIQUE,
                phone VARCHAR(20),
                course VARCHAR(100)
            )
            """
            cursor.execute(create_table_query)
            connection.commit()
            print("✅ Table 'students' created successfully!")
            
            # Insert sample data
            print("\nInserting sample data...")
            sample_data = [
                ("John Doe", "john.doe@example.com", "555-0101", "Computer Science"),
                ("Jane Smith", "jane.smith@example.com", "555-0102", "Mathematics"),
                ("Mike Johnson", "mike.johnson@example.com", "555-0103", "Physics"),
                ("Sarah Wilson", "sarah.wilson@example.com", "555-0104", "Chemistry"),
                ("David Brown", "david.brown@example.com", "555-0105", "Biology")
            ]
            
            insert_query = """
            INSERT IGNORE INTO students (name, email, phone, course) 
            VALUES (%s, %s, %s, %s)
            """
            
            for student in sample_data:
                cursor.execute(insert_query, student)
            
            connection.commit()
            print("✅ Sample data inserted successfully!")
            
            # Verify the setup
            cursor.execute("SELECT COUNT(*) FROM students")
            count = cursor.fetchone()[0]
            print(f"✅ Total students in database: {count}")
            
            print("\n🎉 Database setup completed successfully!")
            print("\nYou can now run the Flask application:")
            print("python app.py")
            
        else:
            print("❌ Failed to connect to MySQL server!")
            
    except Error as e:
        print(f"❌ Error: {e}")
        print("\nTroubleshooting tips:")
        print("1. Make sure MySQL server is running")
        print("2. Check your username and password")
        print("3. Ensure the user has CREATE DATABASE privileges")
        print("4. Try connecting with a different MySQL client first")
        
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("\nDatabase connection closed.")

if __name__ == "__main__":
    setup_database() 