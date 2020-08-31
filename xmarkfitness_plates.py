# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 13:11:10 2020

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
    """get availability of each plates item"""
    soup = get_soup(url)
    results = []
    #container for plates 
    container = soup.find_all('li', {'class':'Odd'})
    for cont in container:
        with contextlib.suppress(AttributeError):
            title = cont.find('a', {'class':'pname'}).text.strip()
            price = cont.find('em', {'class':'p-price'}).text.strip()
            stock = cont.find('div', {'class':'ProductActionAdd'}).text.strip()
            if stock == "Add To Cart":
                stock = "In Stock"
            img_url = cont.find('div', {'class':'ProductImage QuickView'}).a.img['src']
            results.append(dict(title = title, price = price, stock = stock, url = url,
                                company = 'Xmark Fitness', p_type = 'Plates', img_url = img_url))
    return results
    

def main():
    urls = ["https://www.xmarkfitness.com/free-weights/?sort=featured&page={}".format(n) for n in range(1,5)]
    with ThreadPoolExecutor(max_workers=len(urls)) as pool:
        results = pool.map(get_availability_plates, urls)
    results = sum(results, [])
    results = pd.DataFrame(results)
    return results

