# Student CRUD - Flask Mini Project 2

A beginner-friendly Flask application demonstrating **CRUD (Create, Read, Update, Delete)** operations using **Flask Blueprints**, **HTML Forms**, **GET & POST requests**, **Jinja2 Templates**, and **Flash Messages**.

This project is built without a database. Student records are stored in an in-memory Python list of dictionaries to focus on understanding Flask fundamentals before introducing SQLAlchemy.

---

## Features

* View all students
* View student profile
* Add a new student
* Edit existing student details
* Delete a student
* Flash success messages
* Custom error page
* Blueprint-based project structure

---

## Concepts Covered

### Flask

* Blueprints
* Routing
* Dynamic URL Parameters
* GET Requests
* POST Requests
* `request.form`
* `render_template()`
* `redirect()`
* `url_for()`
* Flash Messages
* Application Configuration

### Jinja2

* Template Inheritance
* Variables
* Loops
* Conditional Rendering

### Python

* Lists
* Dictionaries
* List Comprehensions
* Generator Expressions
* `next()`
* CRUD Operations

---

## Project Structure

```text
student-crud/
│
├── app.py
├── config.py
│
├── students/
│   ├── __init__.py
│   ├── routes.py
│   └── data.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── students.html
│   ├── profile.html
│   ├── add.html
│   ├── edit.html
│   ├── about.html
│   └── error.html
│
├── static/
│   └── css/
│       └── style.css
│
└── README.md
```

---

## Routes

| Route                           | Method | Description             |
| ------------------------------- | ------ | ----------------------- |
| `/`                             | GET    | Home page               |
| `/students`                     | GET    | Display all students    |
| `/students/<student_id>`        | GET    | Display student profile |
| `/students/add`                 | GET    | Open Add Student form   |
| `/students/create`              | POST   | Create new student      |
| `/students/edit/<student_id>`   | GET    | Open Edit Student form  |
| `/students/update`              | POST   | Update student details  |
| `/students/delete/<student_id>` | GET    | Delete a student        |
| `/about`                        | GET    | About page              |

---

## Student Data Structure

The application stores data as a list of dictionaries.

Example:

```python
students = [
    {
        "id": 1,
        "name": "Rahul Sharma",
        "age": 22,
        "course": "Python",
        "city": "Delhi"
    }
]
```

---

## CRUD Workflow

### Create

* Open Add Student page
* Submit HTML form
* Read form data using `request.form`
* Append new record to the list
* Redirect to student profile

### Read

* Display all students
* View individual student profile

### Update

* Open Edit Student page
* Modify values
* Submit updated form
* Update matching dictionary
* Redirect to profile page

### Delete

* Find student by ID
* Remove student from list
* Display updated student list

---

## Flask Concepts Used

### Dynamic URL

```python
/student/<int:student_id>
```

### Reading Form Data

```python
request.form.get("name")
```

### Searching a Student

```python
student = next(
    (item for item in students if item["id"] == student_id),
    None
)
```

### Redirect

```python
return redirect(
    url_for("student.profile", student_id=student_id)
)
```

### Flash Message

```python
flash(
    "Student updated successfully!",
    "success"
)
```

---

## Technologies Used

* Python 3.x
* Flask
* HTML5
* CSS3
* Jinja2

---

## How to Run

### Clone the repository

```bash
git clone <repository-url>
```

### Move into the project

```bash
cd student-crud
```

### Install Flask

```bash
pip install flask
```

### Run the application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

---

## Learning Outcomes

After completing this project, you will understand:

* Flask Blueprints
* GET & POST requests
* HTML Forms
* Dynamic Routes
* CRUD Operations
* Redirects
* Flash Messages
* Template Inheritance
* Passing Python data to Jinja templates
* Working with lists and dictionaries in Flask

---

## Future Improvements

* Replace in-memory data with SQLite
* Integrate SQLAlchemy ORM
* Add Flask-WTF forms
* Implement input validation
* Add search functionality
* Add pagination
* Improve UI using Bootstrap
* Implement authentication

---

## Project Status

✅ Completed

This project is the second mini project in my Flask learning roadmap and focuses on mastering CRUD operations before moving to SQLAlchemy and database integration.

---

## Author

**Yogesh Gangwar**

Backend Developer | Python | Flask | PHP | MySQL
