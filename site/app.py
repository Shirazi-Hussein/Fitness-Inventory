# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
from lifting_inv import app
from lifting_inv.models import Product
from flask import Flask, render_template, url_for, flash, redirect


@app.route('/')
@app.route('/home')
def home():
    return render_template('store.html')

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate, public, max-age=0"
    response.headers["Expires"] = '0'
    response.headers["Pragma"] = "no-cache"
    return response

if __name__ == "__main__":
    app.run(debug=True)