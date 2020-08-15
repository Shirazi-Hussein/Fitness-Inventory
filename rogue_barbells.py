# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:05:53 2020

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
    barbell1 = soup.find('div', {'class':'product-shop-accessories'})
    with contextlib.suppress(AttributeError):
        product_title1 = barbell1.find('h1', {'class':'product-title'}).text.strip()
        price1 = barbell1.find('span', {'class':'price'}).text.strip()
        stock1 = soup.find('div', 'bin-stock-availability').div.div.text.strip()
        product_title, price, stock, url = product_title1, price1, stock1, url
        results.append(dict(product_title = product_title, price = price, stock = stock, url = url))
    #container for barbell types 2
    barbell2 = soup.find('div', {'class':'product-shop'})
    with contextlib.suppress(AttributeError):
        product_title2 = barbell2.find('h1', {'class':'product-title'}).text.strip()
        price2 = barbell2.find('span', {'class':'price'}).text.strip()
        stock2 = soup.find('div', 'bin-stock-availability').div.div.text.strip()
        product_title, price, stock = product_title2, price2, stock2
        results.append(dict(product_title = product_title2, price = price2, stock = stock2, url = url))
    return results

def main():
    url = "https://www.roguefitness.com/weightlifting-bars-plates/barbells?limit=160"
    soup = get_soup(url)
    urls = [a['href'] for a in soup('a', 'product-image')]
    with ThreadPoolExecutor(max_workers=len(urls)) as pool:
        results = pool.map(get_availability_barbells, urls)
    results = sum(results, [])
    results = pd.DataFrame(results)
    print(results)

    
        
    
if __name__ == "__main__":
    main()

