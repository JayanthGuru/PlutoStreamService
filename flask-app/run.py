# app/app.py
from flask import Flask
from app.routes import api

server = Flask(__name__)

# Register Blueprints for the API routes
server.register_blueprint(api)

if __name__ == "__main__":
    server.run()
