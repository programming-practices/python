
#------- Operaciones con tupla y lista ----------
# Comprobar si un elemento esta en tupla/lista: in:
# print(4 in tupla_A)
# print(4 in lista_A)
# print()
# print(5 not in tupla_A)
# print(5 not in lista_A)

# Numero de elementos de tupla/lista: len():
# print(len(tupla_A))
# print(len(lista_A))

# Construir una lista ordenada mediante la funcion sort():
# lista_oreginal = [5, 3, 8, 1, 7, 4, 2, 6]
# print(lista_oreginal)
# Function sorted() no modifica la lista_original que se pasa como parametro
# lista_ordenada = sorted(lista_oreginal)
# print('lista_ordenada -> ', lista_ordenada)
# Notar que lista_oreginal no se modifica
# print('Notar que lista_oreginal no se modifica -> ', lista_oreginal)
#------------ Acceso a los elementos de la secuencias ----------
# Los elementos de las secuencias pueden ser accedidos(indexados) mediante el uso de corchetes: lista[<index>]
# En Python, la indexacion se empieze por 0, es decir, el primer elemento tiene indice cero.
# print(lista_ordenada[0])

# Podemos indexar las secuencias utilisando la sintaxis: lista[<inicio>:<final>:<salto>]
# print(lista_ordenada[1:4])
# print(lista_ordenada[1:5:2])
# print(lista_ordenada[1:6:2]) # v ciomy exemplo 2 oznacae.... wchob zrozymitu treba duvutus exemplos

# VNIMANIE Nety vuxoda za razmer lista
# print(len(lista_ordenada))
# print(lista_ordenada[1:8])
# print(lista_ordenada[1:9])
# print(lista_ordenada[1:10])

# Desde el primero hasta el 3
# print(lista_ordenada[:3])

# Desde el primero hasta el ultimo, saltando de 2 en 2:
# print(lista_ordenada[::2])
# print(lista_ordenada[:4:2])
# print(lista_ordenada[2::2])

# Forma inversa de acceso a una secuencia (de atras hacia adelante): Se usa una indice negativo.
# print(lista_ordenada[-1])
# print(lista_ordenada[-2])
# print(lista_ordenada[-3])
# print(lista_ordenada[-3:-1])

# Los elementos de una lista o tupla pueden ser de cualquier tipo, incluyendo otra  lista o tupla
# datosL = [['1', '2', '3'], 'Hola', 4]
# print(datosL)
# sL = datosL[0][1]
# print(sL)
# print(type(sL))
# print('-------------------')
# datosT = (('1', '2', '3'), 'Hola', 4)
# print(datosT)
# sT = datosT[0][1]
# print(sT)
# print(type(sT))

# En algunos cassos nos puede interesar definir tupla de tuplas:
# tupla_1 = (1, 2, 3, 4), 'A', 'B', 'C', 'D', (5, 6, 7, 8, 9)  # mozna neykazyvatu zovniwni dywku
# print(tupla_1)
# tupla_2 = (1, 2, 3, 4), 'A', 'B', 'C', 'D', [5, 6, 7, 8, 9]  # mozna i tak robutu
# print(tupla_2)
# print('---------------------------------------------------')
# lista_1 = [1, 2, 3, 4], 'A', 'B', 'C', 'D', [5, 6, 7, 8, 9]  # mozna neykazyvatu zovniwni dywku
# print(lista_1)
# lista_2 = (1, 2, 3, 4), 'A', 'B', 'C', 'D', [5, 6, 7, 8, 9]  # mozna i tak robutu
# print(lista_2)


