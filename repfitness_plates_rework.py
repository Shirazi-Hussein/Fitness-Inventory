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
    #edit below ----------------------------------------------------------------
    container = soup.find('div', {'class': 'product-shop col-sm-4'})
    for item in container.find_all("tr"):
        with contextlib.suppress(AttributeError):
            product_title = item.contents[0].text.strip()
            price = item.find_next('td').find_next('td').div.div.span.text.strip()
            stock = item.find_next('td').find_next('td').find_next('td').p
            stock2 = 
            if stock != None:
                stock = "Out of Stock"
            elif stock == None:
                stock = "In Stock"
            product_title, price, stock, url = product_title, price, stock, url
            results.append(dict(product_title = product_title, price = price, stock = stock, url = url))
    return results

def main():
    url = "https://www.repfitness.com/bars-plates/olympic-plates"
    soup = get_soup(url)
    urls = [a['href'] for a in soup('a', 'product-image')]
    with ThreadPoolExecutor(max_workers=len(urls)) as pool:
        results = pool.map(get_availability_plates, urls)
    results = sum(results, [])
    results = pd.DataFrame(results)
    print(results)

    
        
    
if __name__ == "__main__":
    main()


