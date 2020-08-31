# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 12:10:06 2020

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
    container = soup.find('div', {'class':'container product-detail product-wrapper'})
    with contextlib.suppress(AttributeError):
        title = container.find('span', {'class':'h1 product-name'}).text.strip()
        price = container.find('span', {'class':'sales'}).text.strip()
        stock = container.find('span', {'class':'availability-msg'}).span.text.strip()
        if stock == "Backorder":
            stock = "Out of stock"
        img_url = soup.find('img', {'class':'d-block img-fluid'})['src']
        results.append(dict(title = title, price = price, stock = stock, url = url,
                            company = 'Titan Fitness', p_type = 'barbells', img_url = img_url))
    return results

def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''    
    for elem in listOfElems:
        if elem in listOfElems:
            listOfElems.remove(elem)
        else:
            pass        

def main():
    url = "https://www.titan.fitness/strength/barbells/"
    soup = get_soup(url)
    urls = ['https://www.titan.fitness/strength/barbells/' + a['href'] for a in soup('a', 'gtm-product-list')]
    checkIfDuplicates_1(urls)
    with ThreadPoolExecutor(max_workers=len(urls)) as pool:
        results = pool.map(get_availability_barbells, urls)
    results = sum(results, [])
    results = pd.DataFrame(results)
    return results
    
        
    



