import math
# Que son modulos:
    # Un archivo con extencion .py .pyc (Python compilado) o archivo escrito en C para CPthon, que posee su poropio espacio
    # de nombre y que puede contener variables, funciones, clases e incluso otros modulos.
# Para que sirven modulos:
    # Para organizar y reutilizar codigo (modularizacion y reutilizacion)
# Como se crea un modulo?
    # Tan sencillo  como crear un archivo con extencion .py (o .pyc o archivo C) y guardarlo donde nos interesa.
# Importacion de modulos
    # Lo habitual cuando se desarollan aplicaciones es que los programas se vuelven muy largos. En este caso conviene organizar
    # el codigo en distintos archvos dependindo de su funcionalidad. Con esto conseguimos:
        # Facilitar el mantenimiento
        # Reutilizar codigo: usar una funcion en varios aplicaciones sin necesidad de copiarla varias veces
    # Estos archivos se llaman modulos y tienen extension .py
        # Contienen definicion de funciones
        # Datos
        # Difinicion de clases, etc.
# Los modulos pueden importar otros modulos. Es constumbre pero no obligatorio el ubicar todas las declaraciones import
# al principio de modulo.
# Los modulos tienen dos roles:
    # Por un lado se pueden importar
    # Por otro aldo se pueden ejecutar
# Modulos estandar:
    # Python viene con una biblioteca de modulos estandar. Algunos modulos se integran en el interprete; esto proveen
    # acceso a operaciones que no son parte de nucleo del lenguaje pero que sin embargo estan integrados, tanto por
    # eficiencia como para proveer acceso a primitivas del sistema operativo, como llamadas al sistema.
    # Para listar los modulos que tenemos instalados y qeu por tanto podemos importar en nuestro programa, basta con
    # ejecutar el siguiente comando: help('modules')
# La funcion integrada dir() se usa para encontrar que nombres define un modulo.
    # Devuelve uan lista ordenada de cadenas.
def sumar(val_1, val_2):
    print("La suma de los numeros es:", val_1 + val_2)

def resta(val_1, val_2):
    print("La resta de los numeros es:", val_1 - val_2)

def multiplicar(val_1, val_2):
    print("La multiplicacion de los numeros es:", val_1 * val_2)


class Vehiculo():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.enmarcha = False
        self.acelerar = False
        self.frenar = False

    def arrancar(self):
        self.enmarcha = True

    def acelerar(self):
        self.acelerar = True

    def frenar(self):
        self.frenar = True

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha,
              "\nAcelerado:", self.acelerar, "\nFrerenado:", self.frenar)

class VuhiculoElectrico(Vehiculo):
    def __init__(self, marca, modelo):
        super().__init__(marca, modelo)
        self.autonomia = 100

    def cargarEnergia(self):
        self.cargando = True

class Furgoneta(Vehiculo):
    def carga(self, cargar):
        self.cargado = cargar
        if self.cargado == True:
            return "La furgoneta esta cargada"
        else:
            return "La furgoneta no esta crgada"

class Moto(Vehiculo):
    haciendoCaballito = ""
    def caballito(self):
        self.haciendoCaballito = "Voy haciendo el caballito"

    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha,
              "\nAcelerado:", self.acelerar, "\nFrerenado:", self.frenar, "\n", self.haciendoCaballito)

class BicicletaElectrica(VuhiculoElectrico, Vehiculo):
    pass

#------------------------------------------ if __name__ == "__main__": -------------------------------------------------
# Para poder ejecutar un modulo, por ejemplo para hacer pruebas con las funciones que estan definidas, tenemos que incluir
# en el modulo el siguiente codigo (normalmente al final):
# if __name__ == "__main__":
#   <llamar_a_funciones_o_clases_dentro_de_modulo>
# ...
# Estos datos que van estar dentro de if no se van ejecutar cuando se hace un import. El if se executa solo cuando executemos
# el modulo donde se encuentra if

# esli v podklychaimom module est napisan prosto print("Hello") to print otrabotaet srazy posle podklychenia modula
# print("Napichataetsa pri podklychenii modula")
# esli ne nyzno chtobu etot print otrabtuval pri podklychenii etoho modula, to nado zdelat tak
if __name__ == "__main__":
    # print("Ne napichataetsa pri podklychenii modula, napichataetsa pri vizove etoho modula")
    # print(help('modules'))
    # print(dir(math))

    # Acceso a la documentacion de la cualquera funcion, en nuestro caso es funcion pow() de math:
    # print(help(math.pow))
    print(math.sin(34))
    print(math.pi)
    print(math.sqrt(24))
