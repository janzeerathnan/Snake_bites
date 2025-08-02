from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from mysql.connector import Error
import os
from config import config

app = Flask(__name__)

# Load configuration
config_name = os.environ.get('FLASK_CONFIG') or 'default'
app.config.from_object(config[config_name])

# Database configuration
DB_CONFIG = config[config_name].get_db_config()

def get_db_connection():
    """Create and return a database connection"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def init_database():
    """Initialize the database and create tables if they don't exist"""
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            
            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS student_db")
            cursor.execute("USE student_db")
            
            # Create students table
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
            print("Database and table created successfully!")
            
        except Error as e:
            print(f"Error creating database: {e}")
        finally:
            cursor.close()
            connection.close()

@app.route('/')
def index():
    """Display all students"""
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM students ORDER BY id DESC")
            students = cursor.fetchall()
            return render_template('index.html', students=students)
        except Error as e:
            flash(f"Error fetching students: {e}", "error")
            return render_template('index.html', students=[])
        finally:
            cursor.close()
            connection.close()
    else:
        flash("Database connection failed", "error")
        return render_template('index.html', students=[])

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    """Add a new student"""
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        
        if not name or not email:
            flash("Name and email are required!", "error")
            return render_template('add.html')
        
        connection = get_db_connection()
        if connection:
            try:
                cursor = connection.cursor()
                insert_query = """
                INSERT INTO students (name, email, phone, course) 
                VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_query, (name, email, phone, course))
                connection.commit()
                flash("Student added successfully!", "success")
                return redirect(url_for('index'))
            except Error as e:
                if "Duplicate entry" in str(e):
                    flash("Email already exists!", "error")
                else:
                    flash(f"Error adding student: {e}", "error")
            finally:
                cursor.close()
                connection.close()
        else:
            flash("Database connection failed", "error")
    
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    """Edit an existing student"""
    connection = get_db_connection()
    if not connection:
        flash("Database connection failed", "error")
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        course = request.form['course']
        
        if not name or not email:
            flash("Name and email are required!", "error")
            return redirect(url_for('edit_student', id=id))
        
        try:
            cursor = connection.cursor()
            update_query = """
            UPDATE students 
            SET name = %s, email = %s, phone = %s, course = %s 
            WHERE id = %s
            """
            cursor.execute(update_query, (name, email, phone, course, id))
            connection.commit()
            flash("Student updated successfully!", "success")
            return redirect(url_for('index'))
        except Error as e:
            if "Duplicate entry" in str(e):
                flash("Email already exists!", "error")
            else:
                flash(f"Error updating student: {e}", "error")
        finally:
            cursor.close()
            connection.close()
    
    # GET request - display edit form
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students WHERE id = %s", (id,))
        student = cursor.fetchone()
        
        if student:
            return render_template('edit.html', student=student)
        else:
            flash("Student not found!", "error")
            return redirect(url_for('index'))
    except Error as e:
        flash(f"Error fetching student: {e}", "error")
        return redirect(url_for('index'))
    finally:
        cursor.close()
        connection.close()

@app.route('/delete/<int:id>')
def delete_student(id):
    """Delete a student"""
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM students WHERE id = %s", (id,))
            connection.commit()
            flash("Student deleted successfully!", "success")
        except Error as e:
            flash(f"Error deleting student: {e}", "error")
        finally:
            cursor.close()
            connection.close()
    else:
        flash("Database connection failed", "error")
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    # Initialize database on startup
    init_database()
    app.run(
        host=app.config.get('HOST', '127.0.0.1'),
        port=app.config.get('PORT', 5000),
        debug=app.config.get('DEBUG', True)
    ) 