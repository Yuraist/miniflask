"""This file contains all the routes for the application.
This will tell Flask what to display on which path.
"""
from flask import render_template

from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')
