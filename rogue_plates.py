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
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

pd.options.display.max_columns = 500

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

def get_availability_plates(url):
    """get availability of each plate item"""
    soup = get_soup(url)
    results = []
    for item in soup('div', 'grouped-item'):
        with contextlib.suppress(AttributeError):
            name = item.find('div', 'item-name').text.strip()
            availability = item.find('div', 'bin-stock-availability').text.strip()
            price = item.find('span', {'class':'price'}).text.strip()
            img_url = soup.find('div', {'class':'prod-header-img'}).img['src']
            if availability != 'Notify Me':
                results.append(dict(name=name, price = price, stock=availability, url=url,
                                    company = 'Rogue Fitness', p_type = 'Plates', img_url = img_url))  
    return results

def main():
    url = 'https://www.roguefitness.com/weightlifting-bars-plates/bumpers?limit=160'
    soup = get_soup(url)
    urls = [a['href'] for a in soup('a', 'product-image')]
    with ThreadPoolExecutor(max_workers=len(urls)) as pool:
        results = pool.map(get_availability_plates, urls)
    results = sum(results, [])
    results = pd.DataFrame(results)
    return results