# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 13:36:36 2020

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

def get_availability_barbells(url):
    """get availability of each barbell item"""
    soup = get_soup(url)
    results = []
    #container for barbell type 1 
    barbell = soup.find('div', {'class': 'product-shop col-sm-4'})
    with contextlib.suppress(AttributeError):
        product_title = barbell.find('h1', {'itemprop':'name'}).text.strip()
        price = barbell.find('span', {'class':'price'}).text.strip()
        stock = barbell.find('div', {'class':'product-info'}).p.text.strip()
        if stock == "Availability: Out of stock":
            stock = "Out of stock"
        if stock == "Availability: In stock":
            stock = "In stock"
        img_url = soup.find('img', {'class':'img-responsive'})['src']
        results.append(dict(p_title = product_title, price = price, stock = stock, url = url,
                            company = 'Repfitness', p_type = 'Barbells', img_url = img_url))
    return results

def main():
    url = "https://www.repfitness.com/bars-plates/olympic-bars"
    soup = get_soup(url)
    urls = [a['href'] for a in soup('a', 'product-image')]
    with ThreadPoolExecutor(max_workers=len(urls)) as pool:
        results = pool.map(get_availability_barbells, urls)
    results = sum(results, [])
    results = pd.DataFrame(results)
    return results



