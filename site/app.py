# -*- coding: utf-8 -*-
"""
Spyder Editor

"""
from lifting_inv import app
from flask import Flask, render_template, url_for, flash, redirect


@app.route('/')
@app.route('/home')
def home():
    return render_template('store.html')

@app.route('/test')
def test_page():
    return render_template('store.html')

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r

if __name__ == "__main__":
    app.run(debug=True)