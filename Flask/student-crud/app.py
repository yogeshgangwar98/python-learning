from flask import Flask
from students import student_bp
from config import Config

app = Flask(__name__)

# register bluprint
app.register_blueprint(student_bp)
app.config.from_object(Config)

if __name__ == "__main__":
    app.run(debug=True)