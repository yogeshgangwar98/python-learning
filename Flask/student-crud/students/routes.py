from flask import render_template, request, flash, redirect, url_for

from . import student_bp
from .data import students

# Home route
@student_bp.route("/")
def home():
    return render_template("home.html")

# List all students
@student_bp.route("/students")
def list_students():
    return render_template("students.html",students=students)

# See deatils of a student by the ID
@student_bp.route("/students/<int:student_id>")
def profile(student_id):
    student = next((item for item in students if item['id']==student_id),None)
    if not student:
        return render_template("error.html")
    return render_template("profile.html", student=student)            

# Open the Edit template
@student_bp.route("/students/edit/<int:student_id>", methods=["GET","POST"])
def edit(student_id):
    student = next((item for item in students if item['id']==student_id),None)
    if not student:
        return render_template("error.html")
    return render_template("edit.html", student=student)  

# On click of update, edit operation is performed
@student_bp.route("/students/update", methods=["POST"])
def update():
    if request.method == "POST":
        student_id = int(request.form.get("id"))
        # iterate through generator until specific id is not found
        student = next((item for item in students if item['id']==student_id),None)
        
        if not student:
            return render_template("error.html")
        student["name"]     = request.form.get("name")
        student["age"]      = int(request.form.get("age"))
        student["course"]   = request.form.get("course")
        student["city"]     = request.form.get("city")
        flash("Student record updated successfully!","success")
        return redirect(url_for("student.profile", student_id=student_id))
    flash("Cannot update student record!","Failure")
    return render_template("error.html")       

# Open add student template
@student_bp.route("/students/add", methods=["GET","POST"])
def add():
    return render_template("add.html")  

# On click on create student add operation is performed
@student_bp.route("/students/create", methods=["POST"])
def create():
    if request.method == "POST":
        new_student = {
            "id"       : students[-1]["id"]+1 if students else 1,
            "name"     : request.form.get("name"),
            "age"      : int(request.form.get("age")),
            "course"   : request.form.get("course"),
            "city"     : request.form.get("city"),
        }
        students.append(new_student)
        flash("Student added updated successfully!","success")
        return redirect(url_for("student.profile", student_id=new_student["id"]))
    flash("Cannot add student record!","Failure")
    return render_template("error.html")  

# Delete the student
@student_bp.route("/students/delete/<int:student_id>")
def delete(student_id):
    global students
    students = [item for item in students if item['id']!=student_id]
    return render_template("students.html", students=students)  

# Route for Edit operation
@student_bp.route("/about")
def about():
    return render_template("about.html")