# Student Profile - Flask Mini Project 1

A beginner-friendly Flask application that demonstrates the core concepts of Flask routing, dynamic URLs, URL parameters, template rendering, and navigation using `url_for()`.

This project is the first mini project in my Flask learning journey and is built without using classes or a database.

---

## Learning Objectives

After completing this project, you will understand:

- Flask application structure
- Route registration using `app.add_url_rule()`
- Function-based views
- Rendering HTML templates
- Dynamic URL parameters
- URL converters (`<int:id>`)
- Query parameters (`request.args`)
- Passing data from Python to HTML
- Jinja2 template syntax
- Template inheritance
- Using static files (CSS)
- Using `url_for()` for navigation

---

## Project Structure

```
student-profile/
│
├── app.py
├── routes.py
├── data.py
├── config.py
│
├── templates/
│   ├── base.html
│   ├── home.html
│   ├── students.html
│   ├── profile.html
│   ├── about.html
│   └── error.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── images/
│
└── README.md
```

---

## Features

- Home page
- View all students
- View individual student profile
- Search student by name
- About page
- Custom error page for invalid student

---

## Technologies Used

- Python 3.x
- Flask
- HTML5
- CSS3
- Jinja2

---

## Routes

| URL | Method | Description |
|------|--------|-------------|
| `/` | GET | Home page |
| `/students` | GET | Display all students |
| `/student/<int:student_id>` | GET | Display student profile |
| `/search?name=Rahul` | GET | Search student by name |
| `/about` | GET | About page |

---

## Sample Student Data

The application uses an in-memory Python dictionary.

Example:

```python
students = {
    1: {
        "id": 1,
        "name": "Rahul",
        "age": 22,
        "course": "Python",
        "city": "Delhi"
    }
}
```

---

## Concepts Practiced

### Flask

- Flask application
- Route registration
- Function-based routes
- `render_template()`
- `request.args`
- `url_for()`

### Routing

- Static routes
- Dynamic routes
- URL converters

### Templates

- Jinja2 variables
- Jinja2 loops
- Template inheritance
- Base template

### Python

- Functions
- Dictionaries
- Loops
- Conditional statements

---

## How to Run

### 1. Clone the project

```bash
git clone <repository-url>
```

### 2. Move into the project

```bash
cd student-profile
```

### 3. Install Flask

```bash
pip install flask
```

### 4. Run the application

```bash
python app.py
```

### 5. Open your browser

```
http://127.0.0.1:5000
```

---

## Sample URLs

Home

```
http://127.0.0.1:5000/
```

Student List

```
http://127.0.0.1:5000/students
```

Student Profile

```
http://127.0.0.1:5000/student/1
```

Search Student

```
http://127.0.0.1:5000/search?name=Rahul
```

About

```
http://127.0.0.1:5000/about
```

---

## Future Improvements

- Add SQLAlchemy database
- Add CRUD operations
- Add Bootstrap styling
- Add student images
- Add form validation
- Implement Flask Blueprints
- Add unit testing

---

## Project Status

Completed

This project is part of my Flask backend learning roadmap before moving to SQLAlchemy, REST APIs, and larger Flask applications.

---

## Author

**Yogesh Gangwar**

Backend Developer | Python | Flask | PHP | MySQL