import os

from flask import Flask, render_template, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route('/')
def view_touchevent():
    from models import Point
    return render_template('touchevent.html', point=point)
