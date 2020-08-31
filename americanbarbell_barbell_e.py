# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 18:19:23 2020

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
    #container for barbell
    with contextlib.suppress(AttributeError):
        product_title = soup.find('h1', {'class':'product-title'}).text.strip()
        price = soup.find('span', {'class':'price'}).text.strip()
        if price == '$ 0.00':
            stock = "Out of stock"
        else:
            stock = "In stock"
        company = 'American Barbell'
        p_type = 'Barbell'
        img_url = soup.find('a', {'class':'fancybox'})['href']
        img_url = 'https:' + img_url
        results.append(dict(product_title = product_title, price = price, stock = stock, url = url, company = company,
                            p_type = p_type, img_url = img_url))
    return results

#check
def main():
    url = "https://americanbarbell.com/collections/bars"
    soup = get_soup(url)
    urls = ["https://americanbarbell.com/" + div.a['href'] for div in soup('div', {'class':'product-image image-swap'})]
    with ThreadPoolExecutor(max_workers=len(urls)) as pool:
        results = pool.map(get_availability_barbells, urls)
    results = sum(results, [])
    results = pd.DataFrame(results)
    return results

    




