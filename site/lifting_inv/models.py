# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
from lifting_inv import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    p_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.String(10))
    stock = db.Column(db.String(20))
    url = db.Column(db.String(100))
    company = db.Column(db.String(20))
    p_type = db.Column(db.String(15))
    img_url = db.Column(db.String(100), default='default.jpg')


