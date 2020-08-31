# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 13:48:10 2020

@author: truet
"""
import contextlib
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

import bs4
import requests

def get_soup(url):
    """get soup of url"""
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, 'lxml')
    return soup

def get_availability_plates(url):
    """get availability of each barbell item"""
    soup = get_soup(url)
    results = []
    with contextlib.suppress(AttributeError):
        product_title = soup.find('div', {'class':'product-name'}).text.strip()
        price = 'Varies'
        stock = soup.find('div', {'class':'product-info'}).p.text.strip()
        if stock == 'Availability: Out of stock':
            stock = "Out of Stock"
        if stock == 'Availability: In stock':
            stock = "In Stock"
        else:
            pass
        try:
            img_url = soup.find('img', {'class':'img-responsive'})['src']
        except:
            img_url = None
        results.append(dict(product_title = product_title, price = price, stock = stock, url = url, company = 'Repfitness', p_type = 'Plates', img_url = img_url))
    return results

def main():
    url = "https://www.repfitness.com/bars-plates/olympic-plates"
    soup = get_soup(url)
    urls = [a['href'] for a in soup('a', 'product-image')]
    with ThreadPoolExecutor(max_workers=len(urls)) as pool:
        results = pool.map(get_availability_plates, urls)
    results = sum(results, [])
    results = pd.DataFrame(results)
    return results