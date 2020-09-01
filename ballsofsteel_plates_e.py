# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 19:34:34 2020

@author: truet
"""
import contextlib
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

import bs4
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_soup(url):
    """get soup of url"""
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(chrome_options=options)
    driver.get(url)
    time.sleep(3)
    page = driver.page_source
    driver.quit()
    soup = bs4.BeautifulSoup(page, 'lxml')
    return soup

def get_availability_plate(url):
    """get availability of each plate item"""
    soup = get_soup(url)
    results = []
    #container for plates
    with contextlib.suppress(AttributeError):
        product_title = soup.find('h1', {'itemprop':'name'}).text.strip()
        price = soup.find('p', {'class':'price'}).text.strip()
        #
        stock = soup.find_all('p', 'stock')
        for s in stock:
            if s.text.strip() != "Out of stock":
                stock = "In Stock"
            else:
                stock = "Out of stock"
        company = 'Bells Of Steel'
        p_type = 'Plates'
        img_url = soup.find('a', 'avada-product-gallery-lightbox-trigger')['href']
        product_title, price, stock, url, company, p_type, img_url = product_title, price, stock, url, company, p_type, img_url
        results.append(dict(product_title = product_title, price = price, stock = stock, url = url, company = company,
                            p_type = p_type, img_url = img_url))
        return results
    
def main():
    url = "https://www.bellsofsteel.com/barbells-and-plates/weight-plates/"
    soup = get_soup(url)
    urls = [a['href'] for a in soup('a', 'product-images')]
    with ThreadPoolExecutor(max_workers=len(urls)) as pool:
        results = pool.map(get_availability_plate, urls)
    results = sum(results, [])
    results = pd.DataFrame(results)
    return results




