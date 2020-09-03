# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 18:58:25 2020

@author: truet
"""
import bs4
import contextlib
import pandas as pd
import requests

def get_availability_barbells(url):
    with contextlib.suppress(AttributeError):
        html = session.get(url).text
        soup = bs4.BeautifulSoup(html, "lxml")
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
        return dict(product_title = product_title, price = price, stock = stock, url = url, company = company, p_type = p_type, img_url = img_url)

url = 'https://www.bellsofsteel.com/barbells-and-plates/barbells/'
session = requests.session()
html = session.get(url).text
soup = bs4.BeautifulSoup(html, "lxml")
urls = [a['href'] for a in soup('a', 'product-images')]

results = []
for url in urls:
    result = get_availability_barbells(url)
    results.append(result)

results = pd.DataFrame(results)
