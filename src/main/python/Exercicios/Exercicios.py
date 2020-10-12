#!/home/dtrl/anaconda3/envs/LessonsPython/bin/python

#1
# resultado = 2 * (3 / 2)
# print('#1 ', resultado)

#2
# resultado = 40 / 3
# print('#2 ', resultado)

#3
# resultado = (4 / 2) ** 5
# print('#3 ', resultado)

#4
# resultado = (-2) ** 2
# print('#4 ', resultado)

#5
# resultado = (-3) ** 3
# print('#5 ', resultado)

#6
# resultado = (4 + 6) / (2 + 3)
# print('#6 ', resultado)

#7
# resultado = 2 + (3 * (6 / 2))
# print('#7 ', resultado)

#8
# resultado = 5 ** 5
# print('#8 ', resultado)

#9
# Escribe una function en Python llamada calcula_iba() que calcule el importe de IVA(21%) de una cierta cantidad.
# Pruebalo con varios valores de entrada.
# def calcula_iba(value, procentaje):
#     return (value * procentaje) / 100
# print(calcula_iba(100, 21))

#10
# Evalua el polinomio x**2 + x**3 + (1/2 x**2) - x en x=10 y en x=7. El resultado ha de ser un numero real.
# def calcula_polinomio(value):
#     return (value**4) + (value**3) + ((1/2)*(value**2)) - value
# print(calcula_polinomio(10))
# print(calcula_polinomio(7))

#11
# Define una function llamada raiz_cubica que devuelva el valor de 3 korin z x
# def raiz_cubica(value):
#     return value ** (1/3)
# print(raiz_cubica(27))

#12
# Convertir grados Farenheit en grados centigrados
# def converterFarenToCent(gradosFarenheit):
#     return (gradosFarenheit - 32)*(5/9)
# print(converterFarenToCent(100))

# 13
# Escribe una funccion que recibe como parametro una lista de elementos y devuelve el valor true si la lista posee elementos
# y flase en caso contrario.
def checkLista(lista):
    if len(lista) <= 0:
        return False
    else:
        return True
# print('checkLista(list(range(0)) -> ', checkLista(list(range(0))))
# print('checkLista(list(range(10)) -> ', checkLista(list(range(10))))
listaEmpty = []
# print('checkLista(listaEmpty)-> ', checkLista(listaEmpty))
listFillings = [1, 2, 4, 7]
# print('checkLista(listFillings) -> ', checkLista(listFillings))
lista21 = [1]
# print('checkLista(lista21) -> ', checkLista(lista21))

#14
# Dada la lista L=[1,2,3,4,5,6,7,8,9] escribe expresiones en Python que produzcan los siguentes resultados:
    # El primer elemento de lista
    # El ultimo elemento de lista (sin conser la longitud )
    # La sublista con los dos ultimos elementos
    # La sublista de los elementos que ocupan posiciones pares
    # La sublista de los elementos que ocupan posiciones impares
L=[1,2,3,4,5,6,7,8,9]
# L=[0,1,2,3,4,5,6,7,8,9]
# print(L[0])
# print(L[-1])
# print([L[-2:]])
listPares = L[::2]
listImpares = L[1::2]
# for i in L:
#     if i % 2 == 0:
#         listPares.append(i)
#     else:
#         listImpares.append(i)
# print(listPares)
# print(listImpares)

#15
# Dada una lista de enteros "listaA" y un numero "numeroN", define:
    # Una funccion que calcule el numero de veces que se repite "numeroN" en "listaA"
    # Una funccion que calcule el procentaje de veces que se repite "numeroN" en "listaA"
listaA = [7, 3, 6, 7, 4, 39, 0, 2, 7, 8, 91, 41, 6, 7]
mumeroN = 7
def countForN(lista, numero):
    return lista.count(numero)
# print(countForN(listaA, mumeroN))
def countForPercent(lista, numero):
    return 100 * lista.count(numero) / len(lista)
# print(countForPercent(listaA, mumeroN))

#16
# Utiliza function range() para generar lista de elementos. Genera de forma automatica la siguente lista [10, 20, 30, 40, 50, 60, 70, 80, 90]
# print(list(range(10,91,10)))

#17
# El methodo upper() del tipo string genera una nueva cadena de caracteres, donde todos los caracteres son mayusculas.
# Dada la siguente cadena.
testo = "Hola, me llamo Francisco Calvo, tu auydaste a mi padre. ... Ahora te voy auydar yo"
# print(testo.upper())
# print(testo.split())
# print(len(testo.split()))
# print(testo.lower())
# print(testo.title())
# print(dir(str))

#18
# Escribe una expresion Python para recuperar el valor del elemento con clave Hola de un diccionario d
    # Comprueba que si d es {} (diccionario vacio) la ejecucion produce un error.
    # Y si d es {'Hola':['Hi', 'Hello'], 'Adios':['Bye']} ?
# d = {}
d = {'Hola':['Hi', 'Hello'], 'Adios':['Bye']}
# print('Hola' in d)
# print(d['Hola'])    # KeyError: 'Hola'

#19
# Escribir una funcion que indique si dos fichas de dominio encajan o no. Las fichas son recibidas en dos tuplas,
# por ejemplo: (1,3) y (5,3)
ficha1 = (1,3)
ficha2 = (5,3)
def encaja(ficha1, ficha2):
    return ficha1[0]==ficha2[0] or ficha1[1]==ficha2[1] or ficha1[0]==ficha2[1] or ficha2[0]==ficha1[1]
# print(encaja(ficha1, ficha2))

#20
# Dados dos diccionarios d1 y d2, escribe una funcion en Python llamada fusion que realice la fusion de los dos diccionarios
# pasados como parametros. Puedes utilizar metodo update().
    # Prueba la funccion con diccionarios d1 = {1:'A', 2:'B', 3:'C'}, d2 = {4:'Aa', 5:'Ba', 6:'Ca'}
    # Utilisa la funccion len() para recuperar el numero de elementos del nuevo diccionario.
    # Prueba la funccion con diccionarios d1 = {1:'A', 2:'B', 3:'C'}, d2 = {2:'Aa', 3:'Ba'}
    # Utilisa lafunccion len()  para recuperar el numero de elemntos del nuevo diccionario.
def fusion(d1, d2):
    d1.update(d2)
d1 = {1:'A', 2:'B', 3:'C'}
d2 = {4:'Aa', 5:'Ba', 6:'Ca'}
fusion(d1, d2)
# print(d1)
# print(len(d1))
d1 = {1:'A', 2:'B', 3:'C'}
d2 = {2:'Aa', 3:'Ba'}
fusion(d1, d2)
# print(d1)
# print(len(d1))

# 21
# Define la funccion media() para calcular la media aritmetica de los elementos de una lista pasada como parametro.
    # Utiliza una bucle for para recorre la lista y calcular la suma de los elementos y el numero de elmentos
    # Inicializa la suma a 0 antes de bucle
    # Inicializa el numero de elementos a 0 antes de bucle
# Otra forma : Usando los funcciones sum() y len()
# Comprueba que se obtiene los siguentes resultados media(a) = 200.0
# Si b = [] entonces media(b) =0. Tambien se acepta que media(b) = []
listaB = [1,2,3,4,5,6,7,8,9,10]
listaB0 = []
def media(lista):
    suma = 0
    numero_Elementos = 0
    if len(lista) == 0:
        return 0.0
    for elem in lista:
        suma = suma + elem
        numero_Elementos = numero_Elementos + 1
    return suma / numero_Elementos
# print(media(listaB))
# print(media(listaB0))
def media2(lista):
    if len(lista) <= 0:
        return 0.0
    return sum(lista) / len(lista)
# print(media2(listaB))
# print(media2(listaB0))

#22
# La funcion farenToCentig() convierte grados Farenheit en grados Centigrados
    # Genera la lista con valores [0...120] con la funcion range
    # Utiliza una bucle for para calcular los grados centigrados de cada elemento de la lista de valores
def farenToCentig(gradosF):
    return (gradosF - 32) / 1.8
listG = list(range(0, 121))
# print(listG)
# for g in listG:
#     print('{0} Farenheit es igual a {1:.2f} Centigrados'.format(g, farenToCentig(g)))

#23
# Los 15 primeros numeros triangulares son: [0,1,3,6,10,15,21,28,36,45,55,66,78,91,105]
    # Define una funcion triang_1() que recibe un numero entero positivo n como parametro y genera la lista de los n primeros
    # numeros triangulares. Resuelve el problema aplicando la formula: a**n = n * (n _+ 1) / 2
    # Define una funcion triang_2() que recibe un numero entero positivo n como parametro y genera la lista de los n primeros
    # numeros triangulares. Resuelve el problema aplicando la formula: a**n = n
    # Utilisa la funcion timeit() para medir tiempos y evaluear que funcion se comporta mejor. Para poder llamar a la funcion
    # usa %timeit en la consola IPython delante de la operacion que quieras evaluear, %timeit triang_2(30)
def triang_1(n):
    a = []
    for i in list(range(n)):
        a.append(int(i*(i+1)/2))
    return a

def triang_2(n):
    a = [0]
    for i in list(range(1,n)):
        a.append(a[i-1]+i)
    return a
print(triang_1(15))
print(triang_2(15))



























