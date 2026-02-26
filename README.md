# HRMS Backend

## Project Overview
The HRMS (Human Resource Management System) Backend is a Python-based application designed to manage and streamline HR processes. This backend provides APIs for managing employees, attendance, and other HR-related functionalities. It is built with scalability and maintainability in mind, making it suitable for small to medium-sized organizations.

## Features
- Employee management: Add, update, and delete employee records.
- Attendance tracking: Record and retrieve attendance data.
- Modular design with separate routes for different functionalities.
- Easy-to-extend schema and models.

## Project Structure
```
hrms-backend/
├── database.py          # Database connection and setup
├── main.py              # Application entry point
├── models.py            # Database models
├── requirements.txt     # Project dependencies
├── schemas.py           # Pydantic schemas for data validation
├── routes/              # API routes
│   ├── attendance.py    # Attendance-related routes
│   ├── employees.py     # Employee-related routes
```

## Prerequisites
- Python 3.9 or higher
- A database system (e.g., PostgreSQL, MySQL, SQLite)

## Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd hrms-backend
   ```
3. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Configure the database connection in `database.py`.
2. Start the application:
   ```bash
   python main.py
   ```
3. Access the API at `http://127.0.0.1:8000`.

## API Endpoints
### Employee Routes
- `GET /employees` - Retrieve all employees
- `POST /employees` - Add a new employee
- `PUT /employees/{id}` - Update an employee
- `DELETE /employees/{id}` - Delete an employee

### Attendance Routes
- `GET /attendance` - Retrieve attendance records
- `POST /attendance` - Add a new attendance record

## Contributing
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to your fork and submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Thanks to the open-source community for providing the tools and libraries used in this project.