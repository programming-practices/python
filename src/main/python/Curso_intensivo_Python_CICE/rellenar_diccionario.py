# -*- coding: utf-8 -*-
"""
Definiendo dos listas de igual longitud, una para nombres, y otra para notas, 
rellenar un diccionario cuyas claves sean los nombres y las notas sean los valores
del mismo. 

"""
# 1. Voy a usar dos listas cualesquiera. Es mas facil si ambas son de la misma
#longitud. Las asigno a variables de nombres de relevantes. 

lista_nombres = ["Álvaro", "Jorge", "Pedro", "Sara", "Ana"]
lista_notas = [7,8,8,4,7]

# Lo que busco es pasar de tener un diccionario vacio a uno que tenga:
# Alvaro: 7, Jorge:8, Pedro:0 y así... correlacionando la primera posicion de 
# cada lista.

# Primero defino un diccionario vacio:

dic = {} # recordemos que el nombre que le doy a la variable es arbitrario, 
# con que me sirva para acordarme de que va, me vale.

# ahora voy a tener que rellenar el diccionario, voy a repasar como se 
# introduce un valor en el mismo:
# dic[key] = value

# ahora, intentaremos hacerlo de modo programático, usando un bucle. 
# se puede hacer con ambos tipos, pero sale mucho mejor con while

i = 0
while i < len(lista_nombres): # da igual que lista coja, ambas son igual de largas
    dic[lista_nombres[i]] = lista_notas[i] 
    i += 1 # que no se os olvide esto!!!
    

# FIN


# NOTAS:
# quiero recordar que para obtener datos de una lista (no diccionarios), 
# vale con nombrar la lista y poner el indice entre corchetes:
# lista_nombres[0] da el primer valor de la lista_nombres, que es Alvaro.
# Asi, dentro del bucle, usamos lista_nombres[i] para obtener cada posicion de esa lista
# y usamos lista_notas[i] para obtener el valor de esa lista en la misma posicion.
