# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 17:32:48 2020

@author: truet
"""
from flask import Flask, render_template, url_for, flash, redirect
from models import Product

@app.route('/')
@app.route('/home')
def home():
    return render_template('store.html')