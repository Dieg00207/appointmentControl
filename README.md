# Medical Appointment Management System - Flask + SQLite

This project is a simple web application developed with Flask and SQLite for patient management and medical appointment tracking.

## Features

- **Add Patient**: Form for entering first name, last name, date of birth, phone number, and email address.
- **Modify Patient**: Edit an existing patient's information.
- **Delete Patient**: Deletes the patient after confirmation.
- **Search Patient**: With a search field that dynamically suggests results using jQuery/AJAX.
- **Simple Interface**: HTML forms and basic navigation.

## Project Structure

```
Flask-Project/
│
├── app.py # Main Flask server logic
├── create_db.py # Script to create database and tables
├── bdd.db # SQLite database
├── templates/ # HTML templates to add, modify, delete, and search for patients
│ ├── index.html
│ ├── add.html
│ ├── modify.html
│ └── delete.html
└── static/ # Static files (if added in the future)
```

## Requirements

- Python 3.7 or higher
- Flask
- SQLite3

### Installation

1. Clone this repository or copy the files to your local environment.
2. Make sure you have Flask installed:

```bash
pip install flask
```

3. Run the `crear_db.py` script to generate the tables in the database.
4. Start the application:

```bash
python app.py
```

5. Open your browser and go to `http://127.0.0.1:5000/`

## Notes

- This system focuses on patient management, but also includes the presence of doctors and appointments in the database.
- Only the patient module has been implemented for demonstration purposes.
