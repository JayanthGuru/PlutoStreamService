from flask import Flask
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from utils.helper import connect_to_db


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/pluto')
def connect():
    return connect_to_db()



if __name__ == '__main__':
    app.run(debug=True)