# app/app.py
from flask import Flask
from app.routes import api

app = Flask(__name__)

# Register Blueprints for the API routes
app.register_blueprint(api)

if __name__ == "__main__":
    app.run(debug=True)
