# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 12:57:12 2020

@author: truet
"""

import contextlib
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

import bs4
import requests
pd.options.display.max_columns = 500

def get_soup(url):
    """get soup of url"""
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.content, 'lxml')
    return soup

def get_availability_plates(url):
    """get availability of each plate item"""
    soup = get_soup(url)
    results = []
    for item in soup('div', 'grouped-item'):
        with contextlib.suppress(AttributeError):
            name = item.find('div', 'item-name').text.strip()
            availability = item.find('div', 'bin-stock-availability').text.strip()
            price = item.find('span', {'class':'price'}).text.strip()
            if availability != 'Notify Me':
                results.append(dict(name=name, price = price, stock=availability, url=url))  
    return results

def main():
    url = 'https://www.roguefitness.com/weightlifting-bars-plates/bumpers?limit=160'
    soup = get_soup(url)
    urls = [a['href'] for a in soup('a', 'product-image')]
    with ThreadPoolExecutor(max_workers=len(urls)) as pool:
        results = pool.map(get_availability_plates, urls)
    results = sum(results, [])
    results = pd.DataFrame(results)
    print(results)

if __name__ == '__main__':
    main()