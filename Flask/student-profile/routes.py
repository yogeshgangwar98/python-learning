from flask import render_template, jsonify, request
from data import students

# Home Page of the application
def home():
    return render_template("home.html")

# Display list of all the students
def list_students():
    return render_template("students.html",students=students)

# Display details of a particular student
def student_profile(student_id):
    student = next((item for item in students if item["id"] == student_id), None)
    if student:  
        return render_template("profile.html",student=student)
    return render_template("error.html"), 404

# Search the student by name
def search_student():
    std_name = request.args.get("name").lower()
    student = next((item for item in students if item["name"].lower() == std_name), None)
    if student:
        return render_template("profile.html",student=student)
    return render_template("error.html"), 404

# Dummy about page
def about():
    return render_template("about.html")


# Register all the routes
def register_routes(app):
    app.add_url_rule(
        "/",
        "home",
        home
    )

    app.add_url_rule(
        "/students",
        "students",
        list_students
    )

    app.add_url_rule(
        "/students/<int:student_id>",
        "profile",
        student_profile
    )

    app.add_url_rule(
        "/search",
        "search",
        search_student
    )

    app.add_url_rule(
        "/about",
        "about",
        about
    )
