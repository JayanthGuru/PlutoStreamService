from flask import Flask

app = Flask(__name__)

from app import routes

if __name__ == '__main__':
    app.run(debug=True if FLASK_ENV == 'development' else False)
    