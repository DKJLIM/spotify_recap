from flask import Flask
from test import test

app = Flask(__name__)

@app.route("/")
def hello_world():
    test()
    return "<p>Hello, World!</p>"

# @app.route('/')