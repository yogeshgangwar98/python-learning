from flask import Flask
from routes import register_routes

# Create the application object
app = Flask(__name__)

# Register all routes into the app
register_routes(app)

# Starting point of the project
if __name__ == "__main__":
    app.run(debug=True)