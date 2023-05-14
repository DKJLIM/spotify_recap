from flask import Flask, request, render_template
from test import test

app = Flask(__name__)


@app.route('/')
def index():
    test()
    return render_template('index.html')


@app.route('/', methods=['POST'])
def submit():
    return "<p>Hello, " + request.form ['text'] + "!</p>"
