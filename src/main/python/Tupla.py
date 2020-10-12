
# Tanto las Tumpla como las listas son conjuntos ordenados de elementos, no asi los diccionarios.

# Una tupla es una variable que permite almeasenar datos inmutables (no pueden ser modificados una ves creados) de tipos
# diferentes. Las tuplas se encierran entre parentesis().
            # Tiene longitud fija
            # Solo tine una dimencion

# Que son las tuplas:
    # Las tuplas son listas inmutables, es decir, no se puede modificar despues de su creacion.
        # No permite anadir, eliminar, mover elementos etc(no append, extend, remove)
        # Si permiten extraer porciones, pero el resultado de la extraccion es una tupla nueva.
        # No permiten busquedas (no incex), en los versiones de puthon antiguos 2,5 2,4 2,3...
        # Si permiten comprobar si un elemento se encuentra en la tupla.
    # Que utulidad o ventajas tinen respecto a las listas?
        # Mas rapidas
        # Menos espacio (mayor optimizacion)
        # Formatean Strings
        # Pueden utilizarse como claves en un diccionario.(las listas no)
#-----------------------------------------------------------------------------------------------------------------------
tupla_A = (4, 'Hola', 6.0, 99)
# print('tupla_A = ', tupla_A)
# print('Tupe de tupla_A = ', type(tupla_A))
# print('tupla_A[0] = ', tupla_A[0])
# Da una error, este indice no existe
# print('tupla_A[7] = ', tupla_A[7])  # IndexError: tuple index out of range
# print(tupla_A[0:10]) # Asi no le da IndexError
# print('---------------------------------------')
#-------------------------------------------- Operaciones sobre tuplas -------------------------------------------------
myTupla = (12, 'Roman', 12, 2000, 12)
# print(myTupla[2])

# Crear una tupla a partir de uan lista
myLista = [1,3,4]
myTupla2 = tuple(myLista)
# print(myTupla2)

# Comprobar si unelemento se encuentra en la tupla
# print('Roman' in myTupla)

# Metodo count() permite buscar la cantidad de mizmos elementos, es decir cuantos elementos(que se pasan como carametro)
# iguales existen en la tupla
# print(myTupla.count(12))

# Metodo len() le dise la longitud de la tupla
# print(len(myTupla))

# Tupla unitaria, o tupla con un unico elemento
tuplaUnElemento = ('Roman',) # para crear tupla con un elemento treba stavutu komy v kinci. A esli ne postavit komy v kinci
# to eto yze ne bydet tupla. Nyzno yznat chto budet esli ne postavit komy
# print(tuplaUnElemento)
# print(len(tuplaUnElemento))

# Una tupla pude ser creada sin parantesis, o se puede dicir empaquetado de tupla
tuplaSinP = "Roman", 12, 45, "Hello"
# print(tuplaSinP)

# Desempaquetar tuplas, a veces interesa asignar un nombre a los elementos de la tuplas para, posteriormente trabajar
# con esas variables:
laborales = (1,2,3,4,5)
lunes, martes, miercoles, jueves, viernes = laborales
# print(martes)
# print(viernes)

# Methodo indice() hace que nosotros podemos aceder al elemento de tupla por un indice, en las verisiones de puthon
# 2,5 2,4 ... no estaba permetido
print(tuplaSinP[2])
#-----------------------------------------------------------------------------------------------------------------------
# ERROR tupla ne vozmozno meniat
# print('Antes ',tupla_A)
# tupla_A[0] = 0.0  # TypeError: 'tuple' object does not support item assignment
# print('Despues ', tupla_A)

# Los elementos de una lista o tupla pueden ser de cualquier tipo, incluyendo otra  lista o tupla
datosT = (('1', '2', '3'), 'Hola', 4)
# print(datosT)
sT = datosT[0][1]
# print(sT)
# print(type(sT))

# En algunos cassos nos puede interesar definir tupla de tuplas:
tupla_1 = (1, 2, 3, 4), 'A', 'B', 'C', 'D', (5, 6, 7, 8, 9)  # mozna neykazyvatu zovniwni dywku
# print(tupla_1)
tupla_2 = (1, 2, 3, 4), 'A', 'B', 'C', 'D', [5, 6, 7, 8, 9]  # mozna i tak robutu
# print(tupla_2)
# print('---------------------------------------------------')
lista_1 = [1, 2, 3, 4], 'A', 'B', 'C', 'D', [5, 6, 7, 8, 9]  # mozna neykazyvatu zovniwni dywku
# print(lista_1)
lista_2 = (1, 2, 3, 4), 'A', 'B', 'C', 'D', [5, 6, 7, 8, 9]  # mozna i tak robutu
# print(lista_2)

#----------------------------------- Concatenacion tuplas con + --------------------------------------------
# Estas operaciones no modifican las secuencias originales.
tupla_1 = (1,2,3,4,5,6)
tupla_2 = (11,22,33,44,55,66)
tupla_result = tupla_1 + tupla_2
# print(tupla_result)
tupla_result1 = (1,2,3,4) + (5,6,7)
# print(tupla_result1)

#--------------------------------------------- Replication (*) de secuencias -------------------------------------------
# Estas operaciones no modifican las secuencias originales.
t = tupla_1 * 4
# print(t)


