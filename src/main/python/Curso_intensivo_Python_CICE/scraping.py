#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''

SCRAPING:

Creemos una lista con un montón (al menos 10) de ciudades, 
saquemos el ROI y el ROI/años y
ordenemos la lista (de mejor a peor inversión)
y la imprimamos 

'''

import requests as r
from bs4 import BeautifulSoup as bs

url = "https://www.numbeo.com/cost-of-living/in/{}?displayCurrency=EUR"

req = r.get(url.format('Rome'))
raw = req.text

soup = bs(raw, 'html.parser') #esto lo hemos copiado, no sabemos qué hace
target_table = soup.findAll("table", {"class": "data_wide_table"})[0]
all_tr = target_table.findAll('tr')

# count = 0
# for tr in all_tr:
#     print(count, tr.text)
#     count += 1

buy = all_tr[60].text
buy = buy.split('   ') # aqui es una lista
buy = buy[1] # esto ya deberia ser un string
buy = buy.split('\xa0') # esto es una lista
buy = buy[0]
buy = buy.replace(',','') # esto quita la coma
buy = float(buy)

rent = all_tr[57].text
rent = rent.split('   ') # aqui es una lista
rent = rent[1] # esto ya deberia ser un string
rent = rent.split('\xa0') # esto es una lista
rent = rent[0]
rent = rent.replace(',','') # esto quita la coma
rent = float(rent)

months_per_year = 12
yearly_rent = rent*months_per_year
apartment_price = 100*buy

ROI = (yearly_rent/apartment_price)*100
ROI_years = apartment_price/yearly_rent

