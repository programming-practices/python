

# a = 3
# if  a > 4:
#     print('es maor que 4')
# elif a < 4:
#     print('es menor que 4')
# elif a == 4:
#     print('es igual a 4')

# primerValue = int(input('Introduce primer value: '))
# segundoValue = int(input('Introduce segundo value: '))
#
# def compareValue(value_1, value_2):
#     if value_1 > value_2:
#         print("{} es mayor que {}".format(value_1, value_2))
#     elif value_2 > value_1:
#         print("{} es mayor que {}".format(value_2, value_1))
#     else:
#         print("{} son iguales {}".format(value_1, value_2))
#
# compareValue(primerValue, segundoValue)

# def func(listaPP):
#     for elemento in listaPP:
#         if type(elemento) == int or type(elemento) == float:
#              print(elemento * -1)
#         elif type(elemento) == str:
#             print(elemento[:3].upper())
#
# listaValues = [1, 2, 3, 4, 5, 6, 7, 'holla', 3.8]
# func(listaValues)

# listaNumeros = range(7, 67)
#
# def func(listaNum):
#     for elemnto in listaNum:
#         if elemnto % 2 == 0:
#             print(elemnto)
#
# func(listaNumeros)

# dic = {'r': 1, 3:'rt'}
# print(dic)

listaNombres = ['Carlos', 'Ana', 'Antonio']
# listaNotas = [4,5,3]
listaNotas = [4,5]
diccionario = {}
for nombre in listaNombres:
    if len(listaNotas) <= listaNombres.index(nombre):
        diccionario[nombre] = None
        continue
    else:
        diccionario[nombre] = listaNotas[listaNombres.index(nombre)]

print(diccionario)