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

### 1. Clone or Download the Project

```bash
# If using git
git clone <repository-url>
cd student-management-system

# Or simply download and extract the files
```

### 2. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure MySQL Database

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

**Note**: The application will automatically create the database and table if they don't exist.

### 4. Run the Application

```bash
python app.py
```

The application will start on `http://localhost:5000`

## Application Structure

```
student-management-system/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── templates/            # HTML templates
    ├── base.html         # Base template with navigation
    ├── index.html        # List all students
    ├── add.html          # Add new student form
    └── edit.html         # Edit student form
```

## Routes

| Route | Method | Description |
|-------|--------|-------------|
| `/` | GET | Display all students |
| `/add` | GET, POST | Add a new student |
| `/edit/<id>` | GET, POST | Edit an existing student |
| `/delete/<id>` | GET | Delete a student |

## Features in Detail

### 1. List All Students (`/`)
- Displays all students in a responsive table
- Shows student ID, name, email, phone, and course
- Action buttons for edit and delete operations
- Empty state with call-to-action when no students exist

### 2. Add New Student (`/add`)
- Form with validation for required fields (name, email)
- Optional fields for phone and course
- Email uniqueness validation
- Success/error flash messages

### 3. Edit Student (`/edit/<id>`)
- Pre-filled form with existing student data
- Same validation as add form
- Updates existing student record

### 4. Delete Student (`/delete/<id>`)
- Confirmation dialog before deletion
- Removes student from database
- Redirects to student list

## Database Configuration

The application uses the following default MySQL configuration:

- **Host**: localhost
- **User**: root
- **Password**: (empty)
- **Database**: student_db (auto-created)

To change these settings, modify the `DB_CONFIG` dictionary in `app.py`.

## Error Handling

The application includes comprehensive error handling for:

- Database connection failures
- Duplicate email addresses
- Missing required fields
- Invalid student IDs
- SQL execution errors

## Security Features

- SQL injection prevention using parameterized queries
- Input validation and sanitization
- CSRF protection through Flask's built-in features
- Secure password handling (when configured)

## Customization

### Adding New Fields

To add new fields to the student table:

1. Update the database schema in `init_database()` function
2. Add form fields to `add.html` and `edit.html` templates
3. Update the form processing in `add_student()` and `edit_student()` functions

### Styling Changes

The application uses Bootstrap 5 for styling. To customize:

1. Modify the CSS in `base.html`
2. Add custom CSS classes
3. Override Bootstrap classes as needed

## Troubleshooting

### Common Issues

1. **Database Connection Error**
   - Ensure MySQL server is running
   - Check database credentials in `app.py`
   - Verify MySQL user permissions

2. **Import Errors**
   - Run `pip install -r requirements.txt`
   - Check Python version (3.7+ required)

3. **Port Already in Use**
   - Change the port in `app.run(debug=True, port=5001)`
   - Or kill the process using the port

### Debug Mode

The application runs in debug mode by default, which provides:
- Detailed error messages
- Auto-reload on code changes
- Interactive debugger

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

For issues and questions:
1. Check the troubleshooting section
2. Review the error logs
3. Create an issue in the repository

---

**Happy Coding!** 🎓 