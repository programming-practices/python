import math

#Las funciones tienen un nombre y se declaran con la palabra raservada def y devuelven un valor usando la palabra
#return. Se puede pasar una lista de argumentos o parametros: bien por posiciones o por clave

#Funcion es conjunto de linesa de codigo agrupadas (bloque de codigo) que funcionen como una unidad realizando una
#tarea especifica.

#Las funciones en Python pueden devolver valores.

#Las funciones en Python pueden tener parametros/argumentos.

#A las funciones tambien se las denomina "metodos" cuando se encuentra definidas dentro de una clase.

#Utilidad: Reutilizacion de codigo(cuando sea necesario o si es necesario)

#Python pasa siempre los valores(parametros/argumentos) por referencia

#Las funciones, junto con las clases, son una de los mecanismos para reutioisar codigo.

#Tienen una lista de argumentos:
    #posicionales
    #por clave
    #argumentos agrupados:
        #tupla de argumentos posicionales (*args)
        #diccionario de argumentos accedidos por clave (**kwargs)
#Los argumentos por clave se usan para indicar valores por defecto  siempre se situan despues de los argumentos posicionales.

# Paso de parametros a una funcion:
    # Variables y paso por referencia
        # En una asignacion de un valor a una variable, se crea una referencia al objeto que se encuentra en el lado derecho
        # de la asignacion. Esto es muy importante entenderlo cuando se trabaja con grandes volumenes de datos.
#----------------------------------------- Variables y paso por referencia ---------------------------------------------
# Ambas variables a y b referencian al mismo objeto. Si se modifica cualquiera de ellas, se modifican los dos.
a = [1, 2, 3]
# print("a-->", a)
b = a
# print("b-->", b)

a[0]= 100
# print("a-->", a)
# print("b-->", b)

b[2] =500
# print("a-->", a)
# print("b-->", b)

# Nota importante: si creamos objeto como subconjunto de otros, NO referencian al mismo objeto:
c = a[:3]
# print("a-->", a)
# print("b-->", b)
# print("c-->", c)

c[1] = 4999
# print("a-->", a)
# print("b-->", b)
# print("c-->", c)

# IMPORTANTE
    # En Python el paso de argumentos a una funcion se hace por referencia, mientras que en otros lenguajes se permite paso
    # por valor y paso por referencia.
def cambiarLista(lista, num):
    lista.append(num)
a = [1, 2, 3, 4, 5]
# cambiarLista(a, 22222)
# print(a)

def cambiarValue(numOld, numNew):
    numOld = numNew
c = 3
b = 0
# print("c = ", c, " and b = ", b)
# cambiarValue(c, b)
# print("c = ", c, " and b = ", b)
#-------------------------------------- Funcinones como argumentos de otras funciones ----------------------------------
# Supongamos que tenemos una lista de ciudades que necesitamos limpiar o formatear.
ciudades = ['   Madrid', 'BARcelonA', 'SeVILLa   ']
# Para dar un formato uniforme a esta lista antes de realizar otras tareas de analisis, es necesario transformarla eliminando
# espacios en blanco y transformando cada nombre a tipo titulo.
# Primera opcion
# def formatear(lista):
#     resultado = []
#     for ciudad in lista:
#         ciudad = ciudad.strip()  # Elimina espacios en blanco
#         ciudad = ciudad.title()  # tipo titulo
#         resultado.append(ciudad)
#     return resultado
# formatear(ciudades)
# ciudades = formatear(ciudades)
# print(ciudades)

operaciones = [str.strip, str.title, str.lower,]
listaNumeros = [1, 2, 3, 4, 5, 45]

def formatear(listaCiudades, operaciones):
    resultado = []
    for ciudad in listaCiudades:
        for op in operaciones:
            ciudad = op(ciudad)
        resultado.append(ciudad)
    return resultado

def formatearSimple(listaCiudades, fun):
    resultado = []
    for ciudad in listaCiudades:
        ciudad = fun(ciudad)
        resultado.append(ciudad)
    return resultado

# print(formatear(ciudades, operaciones))
# print(formatearSimple(ciudades, str.upper))
# print(ciudades)

# El uso de funciones como argumentos de otra funcion es una caracteristica de los lenguajes funcionales. La funcion map
# de los lenguajes funcionales tambien esta accesible en Python. Esta funcion aplica una funcion a una colleccion de objetos.
mi = map(str.strip, ciudades)
# print(list(mi))
# print(type(mi))
lista_Productos = map(lambda x: x * 100, listaNumeros)
# print(list(lista_Productos))


#--------------------------------------------- Funciones anonimas (lambda) ---------------------------------------------
# Las funciones anonimas son aquellas que no tienen nombre y se referen a una unica instruccion. Se declaran con la palabra
# reservada lambda.
# Son funciones cortas

# Funciones normales
def producto(x):
    return x * 2
# funciones anonimas, equivalente al funcion de ariba
resultado = lambda x: x * 2

# Las funciones lambda se utilizan mucho en analisis de datos ya que es muy usual transformar datos mediante funciones
# que tienen a otras funciones en su argumento.
# Se usan funciones lambda en lugar de escribir funciones normales para hacer el codigo mas claro y mas corto.

# Mutiplicar por 2 todos los numeros de la lista:
listaNumeros = [1, 2, 3, 4, 5, 45]
def doublingTheValue(listaNumeros, funcion):
    """Devuelve una nueva lista definida por compresion"""
    return [funcion(x) for x in listaNumeros]       #  ?????????????????
# print(doublingTheValue(listaNumeros, producto))
# El mismo efecto lo consegimos mediante una funcion anonima, evitando asi la definicion de la funcio producto:
# print(doublingTheValue(listaNumeros, lambda x: x * 2))
#------------------------------------------------- *args y **kwargs ----------------------------------------------------
#*args ** kwargs:
    # Usamos *args para representar una tupla arbitraria de argumentos agrupados. No es necesario que el nombre sea args
    # (aunque es frecuente por convenio hacerlo)
def suma_varios (x, y, *others):
    print("x:",x)
    print("y:", y)
    print("others:", others)
# suma_varios(1,2,3,4,5,6,7,8,9,10)

# Se pueden definer los argumentos agrupados despues de los argumentos posiciones y por clave. Usamos **kwargs para representar
# una lista arbitraria de argumentos agrupados representada como un diccionario. Como en el caso anterior, no es necesario
# que el nombre sea kwargs:
def sumar_varios2(x, y, *others, **more):
    print("x:", x)
    print("y:", y)
    print("others:", others)
    print("more:", more)
# sumar_varios2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, cien = 100, mil = 1000)
#--------------------------------------------- Documentacion de funciones ----------------------------------------------
# Cada funcion escrita por un programador deberia realizar una tarea especifica.
# Cuando la cantidad de funciones disponibles para ser utilizadas es grande, puede se dificil saber exactamente que hace
# una funcion. Es por eso que es extremedamente importante documentar en cada funcion:
    # cual es la tarea que realiza
    # cuales son parametros que recibe
    # que es lo que devuelve

# La documentacion de una funcion se coloca despues del encabezado de la funcion, en un parrafo encerrado entre tres
# comillas doubles """ o simples '''.
def cambia(lista, num):
    """Permite anadir un elemento a una lista.\n
       Recibe como parametro una lista y el elemento a anadir\n
       No devuelve nada
    """
    lista.append(num)
# cambia()
# Cuando una funcion definida estacorrectamente documentada, es posible accerder a su documentacion mediante la funcion help().

# Contar con funciones es de gran utilidad, ya que nos permite ir armando una biblioteca de instrucciones con problemas
# que vamos resolvendo, y que se pueden reutilizar en la resolucion de nuevos problemas.
def mean(a1, a2, a3, a4):
    """Calcula la media de cuatro valores
         @:type a1: real
         @:type a2: real
         @:type a3: real
         @:type a4: real
         @:rtype: real
    """
    s = 0.0
    s = s + a1
    s = s + a2
    s = s + a3
    s = s + a4
    return s / 4
#mean()
#---------------------------------------------- Espacio de nombres (namespaces) ----------------------------------------
# Las funciones pueden acceder a variables que se encuentran en dos tipos de ambitos: global y local
    # El ambito local (local namespace) se crea cuando se llama a una funcion.
    # Cuando la funcion termina de ejecutarse, el ambito local se destruye.
# def fun1():
#     t = []
#     s = (1,2,3,4)
#     for i in s:
#         t.append(i)
# En el caso anterior, la lista vacia t se crea en el ambito local de la funcion fun(). Fuera de ella no exste.
# fun1()
# t       # no esta definida, dara un error NameError: name 't' is not defined

# Las variables y los parametros que se declaran dentro de una funcion (ambito local) no existen fuera de ella, no se lo
# conoce. Fuera de la funcion se puede ver solo el valor que retorna y es por eso que es necesario introducir la
# instruccion return
# Si declaramos t fuera de la funcion, en el ambito global:
# t = []
# def fun2():
#     s = (1,2,3,4)
#     for i in s:
#         t.append(i)
# Al llamar a:
# print(t)
# fun2()
# print(t)

# Seguramente tendremos problemas cuando una variable se declara en el ambito local y global de la funcion:
t = 2
def fun1():
    t = []
    s = (1,2,3,4)
    for i in s:
        t.append(i)
# print(t)
# Si queremos que una variable se refiera a la variable global en vez de a local (Python supone que cualquier variable
# cambiada o creada en una funcion es local), debemos anadir la palabra reservada global:
def f():
    global s
    # print(s)
    s = "Esto claro."
    # print(s)
s = "Python es genial!"
f()
# print(s)
#-----------------------------------------------------------------------------------------------------------------------
# Ejemplo de funcion con 2 argumentos posicionales y 2 por claves:
# Los argumentos por claves siempre tienen que ir despues de posicionales
def suma_varios2(x, y, z1 = 0, z2 = 0):
    m = x + y + z1 + z2
    return m

resultado1 = suma_varios2(2, 3)
resultado2 = suma_varios2(2, 3, z2=1)
resultado3 = suma_varios2(2, 3, z1=1)
resultado4 = suma_varios2(2, 3, 1)  # el treser parametro se va asignar al z1
resultado5 = suma_varios2(2, 3, z1=1, z2=1)
resultado6 = suma_varios2(2, 3, 1, 1)
# print(resultado1, resultado2, resultado3, resultado4, resultado5, resultado6)

# Defenicion de una function:
# def sumaTes(x, y, z):
#     m1 = x + y
#     m2 = m1 + z
#     return m2
# print(sumaTes(2, 3, 4))

# resultado = 0  # Ne rabotaet kak v java
# def sumaTodos(x, y, z, t):
#     resultado = x + y + z + t
# print(resultado)
# r = sumaTodos(1, 2, 3, 4)
# print(r, type(r))

# def salydo():
#     print('Hello!!!')
# salydo()

# print(abs(2 - 5))   # valor absoluto
# print(max(3, 5, 1, -6))    # valor maximo de un conjunto de valores
# print(min(3, 5, 1, -6, -6.0))  # valor minimo de un conjunto de valores
# print(round(18.65))    # redondea un float al entero mas cercano
# print(int(18.65))  # convierte al entero mas cercano por de bajo
# print(float(18))  # convierte a decimal, aunque la expresion de entrada sea entera
# print(complex(2))  # convierte a numero complejo
# print(str(256568))  # convierte la expresion a un cadena de characteres

# name = input("What is you name?\n")
# print("Hello, ", name)

# Hay que poner return de forma consistente:
# Bien
# def foo(x):
#     if x >= 0:
#         return math.sqrt(x)
#     else:
#         return None
# # Mal
# def foo(x):
#     if x >= 0:
#         return math.sqrt(x)

#--------------------------------------------------- enumerate() -------------------------------------------------------
# Cuando trabajamos con secuencias de elementos puede resuotar utio conoser el index de cada elemento
# La funccion enumerate() devuelve una secuencia de tuplas de la forma (indice, valor). Mediante un bucle es posible
# recorrerse  dicha secuencia
# ciudades = ["Madrid", "Sevilla", "Segovia", "Valencia"]
# for (i, valor) in enumerate(ciudades):
#     print('%d: %s' %(i, valor))

#---------------------------------------------------- reversed() -------------------------------------------------------
# reversed() devuelve un iterador inverso de una lista
# for (i, valor) in enumerate(reversed(ciudades)):
#     print('%d: %s' %(i, valor))
# ------------------------------------------------ Effecto interesante -------------------------------------------------
# Si en return poner dos resultados methodo devuelve tupla de estos valores
def sum(n1, n2):
    return n1 + n2, n1 - n2

# print(sum(3,4))
# print(sum(3,4)[0])

# ------------------------------------------------- Parametros por defecto ---------------------------------------------
def func(a = "Value por defecto"):
    print(a)
# func()
# func("Hola")