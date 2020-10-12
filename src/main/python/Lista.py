# Tanto las Tumpla como las listas son conjuntos ordenados de elementos, no asi los diccionarios.

# Que son las listas:
#   Estructura de datos que nos permite almacenar grand cantidad de valores(equivalente a los array en todos lenguajes
#   de programacion.
#   En Python las listas pueden guardar diferentes tipos de valores(en otros lenguajes no ocurre esto con los array)
#   Se pueden expandir dinamicamente anadiendo nuevos elementos (otra novedad respecto a los arrays en otros lenguajes)

# En la lista se puede guardar diferentes tipos

# Una lista es similar a una tupla con la diferencia fundamental de que permite modificar los datos una ves creados.
# Las listas se encierren entre corchetes [].
lista_A = [4, 'Hola', 6.0, 99]
# print('lista_A = ', lista_A)
# print('Tupe de lista_A = ', type(lista_A))
# print('1--------------------------------------------')
tupla_A = (4, 'Hola', 6.0, 99)
# print('tupla_A = ', tupla_A)
# print('Tupe de tupla_A = ', type(tupla_A))
# print('2--------------------------------------------')
# print('tupla_A == lista_A ->',tupla_A == lista_A)
# print('tupla_A[0] == lista_A[0] ->',tupla_A[0] == lista_A[0])
# print('3--------------------------------------------')
miLista = ['Maria', 'Pepe', 'Marta', 'Antonio']
# Para aceder a todos elementos de la lista
# print(miLista[:])
# Da una ERROR, este indice no existe
# print(miLista[7])  # IndexError: list index out of range
# print(miLista[0:10]) # Asi no le da IndexError

#---------------------------------------------------- Una matriz -------------------------------------------------------
listaMatriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(listaMatriz)

#------------------------------------------------ Modificacion de lista ------------------------------------------------
# Mientras que una tupla no permite modificar sus elementos, una lista si
# print('Antes ',lista_A)
lista_A[0] = 0.0
# print('Despues ',lista_A)

# print('Antes ', listaMatriz)
# listaMatriz[1] = 2
# listaMatriz[1] = None
listaMatriz[1] = ['A', 'B', 'C']
# print('Despuse ', listaMatriz)

# print('Antes ', listaMatriz)
listaMatriz[1][0] = 'A'
listaMatriz[1][0] = ['A', 'Z']
# print('Despuse ', listaMatriz)

#------------ Acceso a los elementos de la secuencias ----------
# Los elementos de las secuencias pueden ser accedidos(indexados) mediante el uso de corchetes: lista[<index>]
# En Python, la indexacion se empieze por 0, es decir, el primer elemento tiene indice cero.
# print(lista_ordenada[0])

# Podemos indexar las secuencias utilisando la sintaxis: lista[<inicio>:<final>:<salto>]
lista_ordenada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lista_ordenada[1:4])
# print(lista_ordenada[1:5:2])
# print(lista_ordenada[1:6:2]) # v ciomy exemplo 2 oznacae.... wchob zrozymitu treba duvutus exemplos

# VNIMANIE Nety vuxoda za razmer lista
# print(len(lista_ordenada))
# print(lista_ordenada[1:8])
# print(lista_ordenada[1:9])
# print(lista_ordenada[1:10])
# print(lista_ordenada[1:100])  # Asi no le da IndexError

# Desde el primero hasta el 3
# print(lista_ordenada[:3])
# Desde el primero hasta el ultimo, saltando de 2 en 2:
# print(lista_ordenada[::2])
# Desde el primero hasta el 4, saltando de 2 en 2:
# print(lista_ordenada[:4:2])
# Desde el 2 hasta el ultimo, saltando de 2 en 2:
# print(lista_ordenada[2::2])

# Forma inversa de acceso a una secuencia (de atras hacia adelante): Se usa una indice negativo.
# print(lista_ordenada[-1])
# print(lista_ordenada[-2])
# print(lista_ordenada[-3])
# print(lista_ordenada[-3:-1])

# Los elementos de una lista o tupla pueden ser de cualquier tipo, incluyendo otra  lista o tupla
datosL = [['1', '2', '3'], 'Hola', 4]
# print(datosL)
sL = datosL[0][1]
# print(sL)
# print(type(sL))

#----------------------------------------------- Operaciones sobre listas ----------------------------------------------
# Crear una lista a partir de una tupla
tupla_q = (2,3,1)
lista_T = list(tupla_q)
# print(lista_T)

# Anadir un elemento, al final de la lista, con append()
lista_Sem = ['lunes', 'jueves']
# print(lista_Sem)
lista_Sem.append('viernes')
# print(lista_Sem)

# Anadir un elemento, en una determinada position, con insert()
lista_Sem.insert(1, 'martes')
# print(lista_Sem)

# Funcion extend muy parasida a concatenacion, agrega todos elementos indicados en parametros al final de la lista
lista_Sem.extend([1, 2, 3, 4, 5])
# print(lista_Sem)

# Eliminar el elemento de la lista de un determinado posicion con pop():
e = lista_Sem.pop(3)
# print(lista_Sem)
# print(e)
# e vale 'viernes' y lista vale ['lunes', 'martes', 'jueves']

# Si usar funcion pop sin parametros, ella va eliminar ultimo elemento en la lista
# print(lista_Sem)
lista_Sem.pop()
# print(lista_Sem)

# Elimina un elemento a partir de su valor con remove(). Methodo remove() borra primera occurencia
# print(lista_Sem)
# lista_Sem.remove('lunes')
# functio remove nose puede usar sin argumentos
# lista_Sem.remove()  #TypeError:F remove() takes exactly one argument (0 given)
# print(lista_Sem)

# Funcion index nos auyda saber en que indice se encuentra value que buscamos
# print(lista_Sem.index("jueves"))
# print(lista_Sem.index(5))
# print(lista_Sem.index("Cara"))  # ValueError: 'Cara' is not in list

# Si se repiten los values en la lista, la funcion index devuelve primer indice que encuentre
lista_Sem.insert(7, 'martes')
# print(lista_Sem)
# print(lista_Sem.index('martes'))

# Para comprobar si existe value en la lista se usa in
# print(5 in lista_Sem)
# print('martes' in lista_Sem)
# print('R' in lista_Sem)

# Metodo count permite buscar la cantidad de mizmos elementos, es decir cuantos elementos(que se pasan como parametro)
# iguales existen en la lista
myLista = ['q', 'e', 't', 'q', 'c', 'q']
# print(myLista.count('q'))

# Method len() le dice la longitud de lista
# print(len(myLista))

# Ordenar una lista con funccion sort(). No es necesario crear una lista nueva.
listaS = [8, 34, 56, 1, 9, 78, 78.5, 3, 18, 23, 21, 12, 10, 2, 3]
# print(max(listaS))
# print(listaS)
listaS.sort()
# print(listaS)

# Generar listas con range. range() solo admite enteros
#                  inicio,fin,paso
# print(list(range(11)))
# print(list(range(0,11)))
# print(list(range(0,11,2)))

#----------------------------------- Concatenacion de listas con + --------------------------------------------
# Estas operaciones no modifican las secuencias originales.
lista_1 = [1,2,3,4,5]
lista_2 = [11,22,33,44,55]
lista_result = lista_1 + lista_2
# print(lista_result)
lista_result2 = [1, 2, 3] + [4, 5, 6]
# print(lista_result2)

#--------------------------------------------- Replication (*) de secuencias -------------------------------------------
# Estas operaciones no modifican las secuencias originales.
l = lista_1 * 4
# print(l)

#--------------------------------------------------- Help --------------------------------------------------------------

# help(list.remove)
# help(list)
