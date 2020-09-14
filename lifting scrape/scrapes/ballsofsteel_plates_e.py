# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 19:34:34 2020

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
        return dict(p_title = product_title, price = price, stock = stock, url = url, company = company, p_type = p_type, img_url = img_url)

url = 'https://www.bellsofsteel.com/barbells-and-plates/weight-plates/'
session = requests.session()
html = session.get(url).text
soup = bs4.BeautifulSoup(html, "lxml")
urls = [a['href'] for a in soup('a', 'product-images')]

results = []
for url in urls:
    result = get_availability_barbells(url)
    results.append(result)

results = pd.DataFrame(results)


