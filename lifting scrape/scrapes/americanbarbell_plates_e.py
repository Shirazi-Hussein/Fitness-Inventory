# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 21:11:48 2020

@author: truet
"""
import contextlib
import pandas as pd
import bs4
import requests

def get_soup(url):
    """get soup of url"""
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, 'lxml')
    return soup

def main():
    url = "https://americanbarbell.com/collections/weights"
    soup = get_soup(url)
    containers = soup.find_all('div', {'class':'inner product-item'})
    results = []
    s, t, p, u, i = None, None, None, None, None
    for c in containers:
        with contextlib.suppress(TypeError):
            if c.find('strong', {'class':'label sold-out-label'}):
                s = "Out of stock"
            if c.find('a', {'class':'product-title'}).text.strip() == 'Color KG Urethane Pro Series Plates' or c.find('a', {'class':'product-title'}).text.strip() == 'Multiple Adjustable Bench 0-75 Degree - Black Upholstery':
                continue
            else:
                s = "In stock"
                t = c.find('a', {'class':'product-title'}).text.strip()
                p = c.find('div', {'class':'price-regular'}).text.strip()
                u = c.find('a', {'class':'product-grid-image'})['href']
                u = 'https://americanbarbell.com' + u
                i = c.find('img').get('data-src')
                i = 'https:' + i
        results.append(dict(p_title = t, price = p, stock = s, url = u, company = 'American Barbell', 
                            p_type = 'plates', img_url = i))
    results = pd.DataFrame(results)
    return results