
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

# print(ROI_years)



# ------------------------------------------------- Exercicion----------------------------------------------------------
'''
SCRAPING:
    Creemos una lista con un montón (al menos 10) de ciudades,
    saquemos el ROI y el ROI/años y
    ordenemos la lista (de mejor a peor inversión)
    y la imprimamos
'''
list_Ciud = ['Rome', 'Madrid', 'Barcelona', 'Valencia', 'Paris', 'Prague', 'Vienna', 'Leon', 'Malaga', "Albacete"]
# list_Ciud = ['Rome', 'Madrid']
lista_Result_Ciudades =[]
lista_Valores = []
def funScraping(lista_Ciudades):
    for ciudad in lista_Ciudades:
        req = r.get(url.format(ciudad))
        raw = req.text

        soup = bs(raw, 'html.parser')  # esto lo hemos copiado, no sabemos qué hace
        target_table = soup.findAll("table", {"class": "data_wide_table"})[0]
        all_tr = target_table.findAll('tr')

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


        ROI = (yearly_rent / apartment_price) * 100
        ROI_years = apartment_price / yearly_rent

        # Usar clase Ciudad
        # lista_Result_Ciudades.append(Ciudad(ciudad, ROI, ROI_years))

        # Usar lista de tuplas
        tup = (ciudad, ROI, ROI_years)
        lista_Valores.append(tup)

class Ciudad:
    def __init__(self, nombreCiudad, ROI, ROI_years):
        self.nombre = nombreCiudad
        self.ROI = ROI
        self.ROI_years = ROI_years

    def getROI_years(self):
        return self.ROI_years
    def getNombre(self):
        return self.nombre
    def getROI(self):
        return self.ROI

    def __lt__(self, other):
        return self.ROI_years < other.ROI_years
    def __le__(self, other):
        return self.ROI_years <= other.ROI_years
    def __eq__(self, other):
        return self.ROI_years == other.ROI_years
    def __ne__(self, other):
        return self.ROI_years != other.ROI_years
    def __ge__(self, other):
        return self.ROI_years >= other.ROI_years
    def __gt__(self, other):
        return self.ROI_years > other.ROI_years
    def descripcion(self):
        return "Nombre: " + self.nombre +" | ROI: " + str(self.ROI) + " | ROI_years: " + str(self.ROI_years)

# funScraping(list_Ciud)
# print(lista_Result_Ciudades)
# ddd = sorted(lista_Result_Ciudades)
# for cc in ddd:
#     print(cc.descripcion())



# for cc in lista_Result_Ciudades:
#     # print(cc.getNombre + ' ' + cc.getROI_years + ' ' + cc.getROI)
#     print(cc.descripcion())

# ciudad = Ciudad('Nombre', 3333,444)
# print(ciudad.descripcion())

# lista_Valores.sort(key=lambda lista: lista[1], reverse=True)

# ----------------------------------------------------------------------------------------------------------------------
# print(lista_Valores)
# Escribir un csv con los ciudades y su ROI
# head = ['Ciudad', 'ROI', 'ROI_years']
# with open('cities.csv','w') as f1:
#     header = ','.join(head)
#     print(header)
#     f1.write(header + '\n')
#     for line in lista_Valores:
#         file_line = "{},{},{}\n".format(line[0], line[1], line[2])
#         f1.write(file_line)

print("----------------------------------------------")
with open('cities.csv', 'r') as f2:
# with open('src/main/python/Curso_intensivo_Python_CICE/cities.csv', 'r') as f2:
    todos = f2.readline()
    # print(todos)
    for l in todos:
        print(l)