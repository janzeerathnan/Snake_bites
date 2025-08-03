# Student Management System

A complete Python Flask application with MySQL integration for managing student records. This application provides full CRUD (Create, Read, Update, Delete) operations for student data with a modern, responsive web interface using Bootstrap.

## Features

- **Complete CRUD Operations**: Add, view, edit, and delete student records
- **Modern UI**: Responsive design with Bootstrap 5 and Font Awesome icons
- **Database Integration**: MySQL database with automatic table creation
- **Form Validation**: Client-side and server-side validation
- **Flash Messages**: User-friendly success and error notifications
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Database Schema

The application uses a MySQL database with the following table structure:

```sql
CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    phone VARCHAR(20),
    course VARCHAR(100)
);
```

## Prerequisites

Before running this application, make sure you have:

1. **Python 3.7+** installed on your system
2. **MySQL Server** installed and running
3. **pip** (Python package installer)

## Installation

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure MySQL Database

1. Start your MySQL server
2. Create a MySQL user or use the root user
3. Update the database configuration in `app.py`:

```python
DB_CONFIG = {
    'host': 'localhost',
    'user': 'your_username',
    'password': 'your_password',
    'database': 'student_db'
}
```

### 3. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`


