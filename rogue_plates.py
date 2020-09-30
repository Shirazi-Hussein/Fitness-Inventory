# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 12:57:12 2020

@author: truet
"""
import contextlib
import pandas as pd
from concurrent.futures import ThreadPoolExecutor

import bs4
from requests_html import HTMLSession

pd.options.display.max_columns = 500

def get_soup(url):
    """get soup of url"""
    session = HTMLSession()
    r = session.get(url)
    soup = bs4.BeautifulSoup(r.content, 'lxml')
    return soup

def get_availability_plates(url):
    """get availability of each plate item"""
    soup = get_soup(url)
    results = []
    for item in soup('div', 'grouped-item'):
        with contextlib.suppress(AttributeError):
            if item.find('div', {'class':'bin-out-of-stock-message bin-out-of-stock-default'}):
                pass
            elif item.find('button', {'title':'Notify Me'}):
                pass
            else:
                name = item.find('div', {'class':'item-name'}).text.strip()
                availability = "In stock"
                price = item.find('span', {'class':'price'}).text.strip()
                img_url = soup.find('div', {'class':'prod-header-img'}).img['src']
                results.append(dict(p_title=name, price = price, stock=availability, url=url,
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

