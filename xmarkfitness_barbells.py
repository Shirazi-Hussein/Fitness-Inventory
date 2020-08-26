# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 13:31:16 2020

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
    #container for plates 
    container = soup.find_all('li', {'class':'Odd'})
    for cont in container:
        with contextlib.suppress(AttributeError):
            title = cont.find('a', {'class':'pname'}).text.strip()
            price = cont.find('em', {'class':'p-price'}).text.strip()
            stock = cont.find('div', {'class':'ProductActionAdd'}).text.strip()
            if stock == "Add To Cart":
                stock = "In Stock"
            title, price, stock = title, price, stock
            results.append(dict(title = title, price = price, stock = stock, url = url))
    return results
    

def main():
    url = ['https://www.xmarkfitness.com/bars/']
    with ThreadPoolExecutor(max_workers=len(url)) as pool:
        results = pool.map(get_availability_barbells, url)
    results = sum(results, [])
    results = pd.DataFrame(results)
    #how to view only in stock items
# =============================================================================
#     for item in results.index:
#         if results['stock'][item] == "In Stock":
#             print(results['title'][item], results['price'][item])
# =============================================================================
    print(results)
        
    
if __name__ == "__main__":
    main()


