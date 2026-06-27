from flask import Blueprint

# without this init file we have to import from the specific file
student_bp = Blueprint("student",__name__)

from . import routes