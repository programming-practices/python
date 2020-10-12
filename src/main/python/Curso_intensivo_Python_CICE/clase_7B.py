'''
SCRAPING:
    Creemos una lista con un montón (al menos 10) de ciudades,
    saquemos el ROI y el ROI/años y
    ordenemos la lista (de mejor a peor inversión)
    y la imprimamos
'''

import requests as r
from bs4 import BeautifulSoup as bs

city = ["Madrid", "Barcelona", "London", "Albacete"]

list_valores = []

for i in city:
    url = "https://www.numbeo.com/cost-of-living/in/{}?displayCurrency=EUR"

    req = r.get(url.format(i))
    raw = req.text

    soup = bs(raw, 'html.parser')  # esto lo hemos copiado, no sabemos qué hace
    target_table = soup.findAll("table", {"class": "data_wide_table"})[0]
    all_tr = target_table.findAll('tr')

    # count = 0
    # for tr in all_tr:
    #     print(count, tr.text)
    #     count += 1

    buy = all_tr[60].text
    buy = buy.split('   ')  # aqui es una lista
    buy = buy[1]  # esto ya deberia ser un string
    buy = buy.split('\xa0')  # esto es una lista
    buy = buy[0]
    buy = buy.replace(',', '')  # esto quita la coma
    buy = float(buy)

    rent = all_tr[57].text
    rent = rent.split('   ')  # aqui es una lista
    rent = rent[1]  # esto ya deberia ser un string
    rent = rent.split('\xa0')  # esto es una lista
    rent = rent[0]
    rent = rent.replace(',', '')  # esto quita la coma
    rent = float(rent)

    months_per_year = 12
    yearly_rent = rent * months_per_year
    apartment_price = 100 * buy

    ROI = round((yearly_rent / apartment_price) * 100, 2)
    ROI_years = round(apartment_price / yearly_rent, 2)

    tup = (i, ROI, ROI_years)
    list_valores.append(tup)

# print(list_valores)

list_valores.sort(key=lambda lista: lista[1], reverse=True)
print("Lista ordenada por ROI: ")
print(list_valores)

# Escribir un csv con las ciudades y su ROI
head = ['Ciudad', 'ROI', 'ROI_years']

with open('cities.csv', 'w') as f:
    header = ','.join(head)
    print(header)
    f.write(header + '\n')
    for line in list_valores:
        file_line = "{},{},{}\n".format(line[0], line[1], line[2])
        f.write(file_line)

print('\n\n-------------------------------')
with open('cities.csv', 'r') as f:
    todo = f.readlines()
    for l in todo:
        print(l)