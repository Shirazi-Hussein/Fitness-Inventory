# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 18:39:30 2020

@author: truet
"""
import contextlib
import pandas as pd
from concurrent.futures import ThreadPoolExecutor


import requests
import bs4
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


url = 'https://americanbarbell.com/collections/weights'
r = requests.get(url)
soup = bs4.BeautifulSoup(r.content, 'lxml')

containers = soup.find_all('div', {'class':'inner product-item'})
results = []
for c in containers:
    with contextlib.suppress(TypeError):
        if c.find('strong', {'class':'label sold-out-label'}):
            s = "Out of stock"
        else:
            s = "In stock"
        t = c.find('a', {'class':'product-title'}).text.strip()
        p = c.find('div', {'class':'price-regular'}).text.strip()
        u = c.find('a', {'class':'product-grid-image'})['href']
        u = 'https://americanbarbell.com' + u
        i = c.find('img').get('data-src')
        i = 'https:' + i
        stock, title, price, url, image_url = s, t, p, u, i
    results.append(dict(title = t, price = p, stock = s, url = u, company = 'Amerian Barbell', p_type = 'plates', img_url = i))

        

results = pd.DataFrame(results)
print(results)
