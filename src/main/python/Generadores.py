
# Estructura que extrae valor de una funcion y se almacenan en objetos iterables (que se pueden recorrer).
# Estos valores se almacenan de uno en uno
# Cada ves que un generador almacena un valor, esta permanece en un estado pausado hasta que se solicita el siguente.
# Esta caracteristica es conocida como "suspension de estado"
# Generadores Que utilidad tienen
    # Son mas eficientes que las funciones tradicionales
    # Muy utiles con listas de valores infinitos
    # Bajo determinados escenarios, sera muy util que un generador devuelve los valores los valores de uno en uno

# Yield from
    # Utilidad: Simplificar el codigo de los generadores en el caso de utilizar bucles anidados

# Funcion para generar numeros pares
def generaPares1(limite):
    num=1
    listaGen=[]
    while num<limite:
        listaGen.append(num*2)
        num= num+1
    return listaGen
# print(generaPares1(10))

#Funcia con generador
def generaPares2(limite):
    num=1
    while num<limite:
        yield num*2
        num= num+1
devuelvePares = generaPares2(10)
# for i in devuelvePares:
#     print(i, end=" ")
# print(next(devuelvePares))
# print("Aqui podria ir mas codigo...")
# print(next(devuelvePares))
# print("Aqui podria ir mas codigo...")
# print(next(devuelvePares))
# print("Aqui podria ir mas codigo...")

# En Python cuando colocamos un asterisco adelante de un argumento de una funcion, estamos indicando al programa que va
# recibir un numero inderterminado de elementos, es decir nose si va recibir un elemento o dos elementos o siete elementos
# no lo sabemos. Y ademas de indicar esto estamos disiendo  que esos argumentos que no sabemos cuantos vamos a recibir en forma tupla
def devuelveCiudades1(*ciudades):
    for elemento in ciudades:
        yield elemento
ciudadesDevueltas = devuelveCiudades1("Madrid", "Barcelona", "Bilbao", "Valencia")
# print(next(ciudadesDevueltas))
# print(next(ciudadesDevueltas))

# -----------------------------------Explicando yield from
def devuelveCiudades2(*ciudades):
    for elemento in ciudades:
        for subElemento in elemento:
            yield subElemento
ciudadesDevueltas = devuelveCiudades2("Madrid", "Barcelona", "Bilbao", "Valencia")
# print(next(ciudadesDevueltas))
# print(next(ciudadesDevueltas))

def devuelveCiudades3(*ciudades):
    for elemento in ciudades:
        yield from elemento
ciudadesDevueltas = devuelveCiudades3("Madrid", "Barcelona", "Bilbao", "Valencia")
print(next(ciudadesDevueltas))
print(next(ciudadesDevueltas))