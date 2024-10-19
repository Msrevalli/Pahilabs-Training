# app/routes.py

from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/hello/')
@main.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)
