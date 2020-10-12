
# En Python los bloques se delimitan por sangrado, no con llaves ni sentencias tipo and

# Bucle for
    # Recorriendo strings
    # Tipo range         apartir de version 3.0 3.1 tipo range , antes era una funccion
    # Notaciones especiales con print

#----------------------------------------------------- Bucle for -------------------------------------------------------
# El bucle for permite realizar una tarea un numero fijo de veces. Se utioiza para recorrer objetos iterables, es decir,
# una colecction de elementos:
# for <elemento> in <objeto_iterable>:
#       <hacer algo...>
# El objeto_Iterable puede ser tupla, una lista, un diccionario, etc
# El bucle se repite  un numero fijo de veces, que es la longitud de la coleccion de elementos.

# El valor de indice en cada repiticion es el correspondiente a la posicion de la coleccion.
lista = list(range(0,10))
# print(lista)
# for indice in lista:
#     print(indice)
    # print('Hola por n vez')

# Example de suma de todos elementos de la tupla:
suma = 0
# for elemento in (1,2,3,4,5):
    # suma = suma + elemento
    # suma += elemento
# print(suma)

# Examplo con una lista de strings:
dias = ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes']
# for nombres in dias:
#     print(nombres)

# Ejemple que crea la lista de enteros en el intervalo (0,3)
# for i in range(0,3):
#     print(i)

# Tambien es posible recorrer una tupla de elementos:
puntos = ((0,1), (1,2), (1,3))
# for (x, y) in puntos:
#     print('(', x, ',',  y, ')')

# La instruccion continue permite saltar de una iteracion a otra
# En esta ejemplo, print() no se ejecuta si j es un numero par
# for j in range(10):
#     if j % 2 == 0:
#         continue
#     print(j)

# Bucle for sobre un diccionaro
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



# for i in ["primavera", "verano", "otono", "invierno"]:
#     print("Hello")
    # print(i)

# for i in [1,2,3,4,5]:
#     print("Hola", end="")

# for i in "Hola. Como estas?":
#     print("Hola", end=" ")
    # print(i, end="")

# email = False
# myEmail = "dragon.cuenca.ua@gmail.com"
# myEmail = input("Introduce tu direccion de email: ")
# for i in myEmail:
#     if i == "@":
#         email = True
# if email:
#     print("Email esta correcto")
# else:
#     print("Email esta incorecto")

# Range es un tipo que funcciona muy paracido al array, es decir range(5) va crear un array de 5 elementos
# for i in range(5):
    # print("Hola")
    # print(i)
    # print(type(i))

#----------------------------------------------------- Bucle while -------------------------------------------------------
# La llamada a while se repita el bloque de instucciones mientras se cumple una condicion
# while <condicion>:
#       <algo que hacer>

# El numero de iteraciones es variable, depende de la condiccion
# i = -2
# while i < 4:
#     print(i)
#     i = i + 1
    # i += 1
# print('Esto fuera del while')

# Se puede interrupir la ejecucion completa de un bucle for o while con la instruccion break
i = 0
while i < 5:
    print(i)
    i = i + 1
    if i == 3:
        break

# La palabra clave pass devuelve un Nullo. Po iskat informaciy ob etom zarezervirovanom slove
# while True:
#     pass