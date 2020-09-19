# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET KEY'] = "123456789101112131415"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['TEMPLATES_AUTO_RELOAD'] = True

db = SQLAlchemy(app)

