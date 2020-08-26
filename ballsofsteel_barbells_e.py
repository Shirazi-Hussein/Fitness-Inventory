# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 18:58:25 2020

@author: truet
"""
import contextlib
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

import re
import bs4
import requests
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_soup(url):
    """get soup of url"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    time.sleep(3)
    page = driver.page_source
    driver.quit()
    soup = bs4.BeautifulSoup(page, 'lxml')
    return soup

def get_availability_barbells(url):
    """get availability of each barbell item"""
    soup = get_soup(url)
    results = []
    #container for barbell 
    with contextlib.suppress(AttributeError):
        product_title = soup.find('h1', {'itemprop':'name'}).text.strip()
        price = soup.find('span', {'class':'woocommerce-Price-amount amount'}).text.strip()
        stock = soup.find('div', {'class':'avada-availability'}).p.text.strip()
        company = 'Bells Of Steel'
        p_type = 'Barbell'
        img_url = soup.find('a', 'avada-product-gallery-lightbox-trigger')['href']
        if stock == 'Out of stock':
            pass
        else:
            stock = 'In Stock'
        product_title, price, stock, url, company, p_type, img_url = product_title, price, stock, url, company, p_type, img_url
        results.append(dict(product_title = product_title, price = price, stock = stock, url = url, company = company, p_type = p_type, img_url = img_url))
        return results
    
def main():
    url = "https://www.bellsofsteel.com/barbells-and-plates/barbells/"
    soup = get_soup(url)
    urls = [a['href'] for a in soup('a', 'product-images')]
    with ThreadPoolExecutor(max_workers=len(urls)) as pool:
        results = pool.map(get_availability_barbells, urls)
    results = sum(results, [])
    results = pd.DataFrame(results)
    print(results)

    
        
    
if __name__ == "__main__":
    main()
