
# Que son los diccionarios:
    # Estructura de datos que nos permite almacenar valores de diferente tipo(entero, cadena de texto, decimales) e incluso
    # listas i otros diccionarios.
    # La principal caracteristica de los dicionarios es que los datos se almasenan asociados a un calave de tal forma
    # que se crea una asociacion de tipo clave:valor para cada elemento almacenado.
    # Los elementos almacenados no estan ordenados. El orden es indiferente ala hora de almacenar informacion en un diccionario.

# En diccionario no se puede guardar dos claves iguales, pero dos values iguales si se puede guardar.
# La clave de un dicionario puede ser cualquer variable de tipo inmutable: cadenas, enteros, tuplas
# Los valores de un diccionario pueden ser de cualquier tipo: lista, cadenas, tuplas, otros diccionarios, objectos etc
# En un diccionario no existe una posicion indexada porque no es una collectio ordenada.
# Las claves son unicas dentro de un diccionario, es decir que no puede haber un diccionario que tenga dos veces la misma
# clave, si se asigna un valor a una clave ya existe, se remplaza el valor anterior.

myDiccionario = {"Ucrania":"Kiev", "Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"London", "Espania":"Madrid"}
# print(myDiccionario["Francia"])

# Para anadir un elemento al final de diccionario
myDiccionario["Italia"] = "Lisboa"
# print(myDiccionario)

# Para cambiar un valor de diccionario
myDiccionario["Italia"] = "Roma"
# print(myDiccionario)

# Para eliminar un valor del diccionario
del myDiccionario["Reino Unido"]
# print(myDiccionario)

# Diccionario con diferentes tipos de valores
myDiccionarioDEF = {"USA":"Wahington", 23:"Jordan", "Mosquetos":3}
# print(myDiccionarioDEF)

# Diccionario con la clave de tipo tupla(tambien se puede utilizr la lista como tipo de clave, pero la lista esta modificable)
myTupla = ("Espania", "Francia", "Reino Unido", "Alemania")
myDiccionarioT = {myTupla[0]:"Madrid", myTupla[1]:"Paris", myTupla[2]:"London", myTupla[3]:"Berlin"}
# print(myDiccionarioT)
# print(myDiccionarioT[myTupla[2]])
# print(myDiccionarioT["Reino Unido"])

# Diccionario con value Tupla
myDiccionarioE = {23:"Jonatan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":[1991, 1992, 1993, 1996, 1997, 1998]}
# print(myDiccionarioE)
# print(myDiccionarioE["anillos"])

# Diccionario con value Diccionario
myDiccionarioDD = {23:"Jonatan", "Nombre":"Michael", "Equipo":"Chicago", "anillos":{"temporadas":[1991, 1992, 1993, 1996, 1997, 1998]}}
# print(myDiccionarioDD)
# print(myDiccionarioDD["anillos"])


# Metodo keys() devuelve una lista con las claves de diccionario
# print(myDiccionarioDD.keys())

# Metodo values() nos ensenia todos values del diccionario
# print(myDiccionarioDD.values())

#Methodo len() devuelve una lista con las values de diccionario
# print(myDiccionarioDD.values())
# print(len(myDiccionarioDD))

# Se puede crear un diccionario vacio y despues asignarle valores:
diccionario = {}
diccionario["W"] = 1
diccionario['Q'] = 2
diccionario['M'] = 3
diccionario['A'] = "a"
# print(diccionario)

# El operator in devuelve si un diccionario tine una clave
# print('A' in diccionario)

# El methodo get(), devuelve el valor para la clave dada o None si la clave no esta en diccionario
# print(diccionario.get('A'))
# print(diccionario.get('B'))

# Methodo pop() elimina elemento de un diccionario, y en mismo tiempo devuelve valor eliminado
# print(diccionario)
EL = diccionario.pop("Q")
# diccionario.pop()   # ERROR
# print(diccionario)
# print(EL)

# Se pueden fusionar diccionarios con el methodo update()
diccionario11 = {"A": 56, "X": 43}
diccionario22 = {"Q": 856, "D": 943, "V": 943}
diccionario11.update(diccionario22)
print(diccionario11)
print(diccionario22)

# Ne rabotaet tak
# diccionario33 = diccionario11 + diccionario22
# print(diccionario33)

# ------------------------------------Bucle for sobre un diccionaro
# Un diccionario, que es un objeto iterable, se puede recorrer tambien. En este ejemplo usamos el methodo items() que
# nos devuelve los elementos del diccionario como una lista de tuplas clave-valor.
diccionario = {1:'Lunes', 2:'Martes', 3:'Miercoles', 4:'Jueves', 5:'Viernes', 6:'Sabado', 7:'Domingo'}
# for i in diccionario:
#     print(i)
# for i in diccionario.items():
#     print(i)   # Devuelve cada tupla de valores (clave, value)
# for clave, valor in diccionario.items():
#     print(clave, valor)

# Se puede recorrer solo las claves si usamos methodo key()
# for claves in diccionario.keys():
#     print(claves)

# Se puede recorrer solo los values si usamos methodo key()
# for value in diccionario.values():
#     print(value)