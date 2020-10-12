
# Una clase es la difinicion abstracta de un objeto.
    # Una clase la estructura y el comportamiento de los objetos
    # En terminos de programacion, uno empieza definiendo una clase y luego procede a crear objetos de dicha clase.
# El conjunto de atributos y methodos de una clase son los miembros de una clase. Todos los objetos que pertenecen a una
# clase tienen los mismos miembros.
    # Mismos methodos
    # Mismos tipos de atributos
# A los objetos de una clase tambien se les llama instancias de la misma.
# Los objetos creados o estanciados se almacenan en variables, como hacemos con el resto de tipos
# En Python se define una clase con la palabra reservada class seguida de su nombre, dos puntos(:) y a continuacion,
# indentado, el cuerpo de la clase.
# El metodo __init__() es un methodo especial(llamado constructor de la clase en otro lenguaje): se ejecuta automaticamente
# al crear un objeto.
# Creacion de un objeto:
    # Hay que invocar a la clase como si fuera una funcion, pasando los argumentos que defina el methodo __init__().
    # El valor de retorno sera el objeto reciente creado.
# Destruccion de un objeto:
    # Se realiza automaticamente cuando las variables a las que se le asigna la instancia sale del ambito de ejecucion.
# Parametro self:
    # El parametro self es obligatorio en la difinicion de todos los methodos de la clase, pero no el programador no lo
    # pasa explicitamente al llamar a un methodo.
    # Contiene una referencia al propio objeto, por lo que se utiliza para acceder a cualquier atributo o metodo del propio
    # objeto, como en el caso del methodo __init__(), donde accede a los atributos del propio objeto para asignarle los
    # valores pasados por parametros
# Atributos:
    # Por convencion todos los atributos de una clase se deben inicializar en el methodo __init__(). Sin embargo, esto
    # no es un requisito, ya que los atributos solo comienzan a existir cuanco se les asigna primer valor.
    # Es una buena practica asignar un valor inicial a todos los atributos de un objeto; esto evitara futuros errores
    # cuando se quiera acceder a un atributo no inicializado.
# Getters y setters
    # A veces queremos que se acceda a un atributo de forma controlada: escribiremos un methodo para obtener el valor de
    # una variable y otro methodo para escribirlo. Por convencion se suelen llamar getVariable() y setVariable().
# Methodos especiales
    # Python cuenta con una serie de methodos especiales, con el fin de emular cierto tipo de funcionalidades presentes
    # en tipos de datos estandart como los diccionarios, las listas o los numeros.
    # __repr__(self)
    # Methodo especial que se invoca cuando llamamos a repr(<objeto>) e intenta emular la funcionalidad de la funcion interna
    # repr(), que devuelve una representacion en modo texto de nuestros objetos, similar a print()
    # __len__(self) Methodo especial que se invoca cuando llamamos a len(<objeto>) e intenta emular la funcionalidad de
    # la funcion interna len(). Tiene sentido implementarlo si un objeto de esa clase tuviera razonablemente longitud o tamano.
    # __eq__(self, otro)
    # __lt__(self, otro)
    # __le__(self, otro)
    # __gt__(self, otro)
    # __ge__(self, otro)
    # __ne__(self, otro)
    # Methodos que se invocan cuando realizamos operaciones de comparacion con los objetos de una clase y busca emular
    # la funcionalidad de la funcion interna cmp().
    # Son los methodos enriquecida:
        # Los operaciones:
            # x < y llama al methodo especial x.__lt__(y)
            # x <= y llama a x.__le__(y)
            # x == y llama a x.__eq__(y)
            # x != y llama a x.__ne__(y)
            # x > y llama a x.__gt__(y)
            # x >= y llama a x.__ge__(y)

#--------------------------------------------------- Atributos ---------------------------------------------------------
class Vehiculo():
    def __init__(self, aColor, aAncho, aVelocidad, aPlazas):
        self.__color = aColor
        self.__ancho = aAncho
        self.__velocidad = aVelocidad
        self.__plazas = aPlazas


    def cambiaColor(self, nuevoColor):
        self.__color = nuevoColor

    def __methodoPrivado(self):
        print("Privado")

    def descripcion(self):
        print("Color de vehiculo es:", self.__color, "\nAncho de veiculo es:", self.__ancho,
              "\nVelosidad de veiculo es:", self.__velocidad, "\nVehiculo tiene:", self.__plazas, "plazas")

# ------------------------------------------------- Metodos especiales --------------------------------------------------
    # Podemos anadir esta difinicion de nuestro methodo especial __repr__() en nuestra clase Vehiculo asi:
    # Esta funccion esta muy parecida a method toString() en Java
    def __repr__(self):
        return "Vehiculo de color %s, plazas: %d" %(self.__color, self.__plazas)
    # Para nuestra clase Vheiculo podemos anadir nuestro methodo especial len() asi:
    # Ahora si llamamos a len(miVehiculo) nos devuelve cantidad de las plazas
    def __len__(self):
        return self.__plazas
    # Para nuestro clase Vehiculo podemos anadir estos methodos especiales:
    def __lt__(self, other):
        return self.__plazas < other.__plazas
    def __le__(self, other):
        return self.__plazas <= other.__plazas
    def __eq__(self, other):
        return self.__plazas == other.__plazas
    def __ne__(self, other):
        return self.__plazas != other.__plazas
    def __ge__(self, other):
        return self.__plazas >= other.__plazas
    def __gt__(self, other):
        return self.__plazas > other.__plazas
#-----------------------------------------------------------------------------------------------------------------------

miVehiculo = Vehiculo("Azul", 1.30, 220, 4)
miVehiculo2 = Vehiculo("Azul", 1.30, 220, 4)
# miVehiculo.descripcion()
# print("---------------------------------")
# miVehiculo.cambiaColor("Blanco")
# miVehiculo.descripcion()
# print("---------------------------------")
# miVehiculo.__methodoPrivado()  # Dara este error: AttributeError: 'Vehiculo' object has no attribute '__methodoPrivado'
# Todavia podemos acceder al methodo __methodoPrivado con esta trampa
# miVehiculo._Vehiculo__methodoPrivado()
#------------------------------------------------- Metodos especiales --------------------------------------------------
# print(miVehiculo)
# print(miVehiculo.__len__())
# print(miVehiculo.__lt__(miVehiculo2))
# print(miVehiculo.__le__(miVehiculo2))
# print(miVehiculo.__eq__(miVehiculo2))
# print(miVehiculo.__ne__(miVehiculo2))
# print(miVehiculo.__ge__(miVehiculo2))
# print(miVehiculo.__gt__(miVehiculo2))
#------------------------------------------------- Getters y Setters ---------------------------------------------------
class Fecha:
    def __init__(self, aFecha):
        self.__fecha = aFecha

    def getFecha(self):
        return self.__fecha

    def setFecha(self, newFecha):
        if newFecha > 0 and newFecha < 31:
            self.__fecha = newFecha
        else:
            print("Error: Fecha tiene que estar en diapasono de 0 a 31")

# fecha = Fecha(34)
# print(fecha.getFecha())
# fecha.setFecha(12)
# print(fecha.getFecha())

# El codigo anterior se puede simplificar mediante el uso de las propiedades (property). Notar que el siguente ejemplo
# dara error.
class Fecha:
    def __init__(self, aFecha):
        self.__fecha = aFecha

    def getFecha(self):
        return self.__fecha

    def setFecha(self, newFecha):
        if newFecha > 0 and newFecha < 31:
            self.__fecha = newFecha
        else:
            print("Error: Fecha tiene que estar en diapasono de 0 a 31")
    # Aqui ya no necisitamos poner dos giones bajos, porque la atributo fecha ya esta protegida
    # Aqui pasamos a parametros los nombres de funcciones. En Python se permite
    fechaProperty = property(getFecha, setFecha)
# miFecha = Fecha(33)
# miFecha.fechaProperty = 12
# print(miFecha.getFecha)
#-----------------------------------------------------------------------------------------------------------------------
# class Coche():
#     largoChasis = 250
#     anchoChasis = 120
#     ruedas = 4
#     enmarcha = False
#
#     # palabra rezervada self esta muy parecida al this. Palabra self maie ykazyvatusa ves chas potomu chto vona ne
#     # doaiotsa po ymolchaniy
#     def arrancar(self):
#         # pass # palabra rezervada pass hace que cuando llamamos a una funccion vacia no nos da error
#         self.enmarcha = True
#
#     def estado(self):
#         if(self.enmarcha):
#             return "El coche esta en marcha"
#         else:
#             return "El coche esta parado"

# miCoche = Coche()  # instanciar una clase
# print("El largo de coche es:", miCoche.largoChasis)
# print("El coche tiene", miCoche.ruedas, "ruedas")
# miCoche.arrancar()
# print(miCoche.estado())
# print("---------------- A continuacion creamos el segundo objeto ---------------")
# miCoche2 = Coche()
# print("El largo de coche es:", miCoche2.largoChasis)
# print("El coche tiene", miCoche2.ruedas, "ruedas")
# print(miCoche2.estado())
#-----------------------------------------------------------------------------------------------------------------------
# class CocheA():
#     # Esto es constructor
#     def __init__(self):
#         self.__largoChasis = 250
#         self.__anchoChasis = 120
#         # Dos giones bajos adelante de variable segnifican que variable esta incapsulada(privada), es decir que fuera de
#         # classe no se puede llamar o cambia esta variabel. Pero dentro de su classe si se puede cambiar
#         self.__ruedas = 4
#         self.__enmarcha = False
#
#     def arrancar(self, arrancamos):
#         self.__enmarcha = arrancamos
#         if (self.__enmarcha):
#             return "El coche esta en marcha"
#         else:
#             return "El coche esta parado"
#
#     def estado(self):
#         print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, "y un largo de", self.__largoChasis)
#
# miCocheA = CocheA()
# print(miCocheA.arrancar(True))
# miCocheA.estado()
# print(---------------- A continuacion creamos el segundo objeto ---------------")
# miCocheA2 = CocheA()
# print(miCocheA2.arrancar(False))
# miCocheA2.__ruedas = 2  # Ahora esta linea de codigo no cambia la variable, la variable __ruedas esta encapsulada
# miCocheA2.estado()
#-----------------------------------------------------------------------------------------------------------------------
class Coche():
    # Esto es constructor
    def __init__(self):
        self.__largoChasis = 250
        self.__anchoChasis = 1201
        # Dos giones bajos adelante de variable segnifican que variable esta incapsulada(privada), es decir que fuera de
        # classe no se puede llamar o cambia esta variabel. Pero dentro de su classe si se puede cambiar
        self.__ruedas = 4
        self.__enmarcha = False

    def arrancar(self, arrancamos):
        self.__enmarcha = arrancamos
        if(self.__enmarcha):
            chequeo = self.__chequeoInterno()
        if (self.__enmarcha and chequeo):
            return "El coche esta en marcha"
        elif(self.__enmarcha and chequeo == False):
            return "Algo ha ido mal en el chequeo. No podemos arrancar"
        else:
            return "El coche esta parado"

    def estado(self):
        print("El coche tiene ", self.__ruedas, "ruedas. Un ancho de ", self.__anchoChasis, "y un largo de", self.__largoChasis)

    # Dos giones bajos adelante de nombre de la funccion significa que funcion esta incapsulada, igual como con los variables
    def __chequeoInterno(self):
        print("Realisando chequeo interno")
        self.gasolina = "ok"
        self.aceite = "ok"
        self.puertas = "cerradas"
        if(self.gasolina == "ok" and self.aceite == "ok" and self.puertas == "cerradas"):
            return True
        else:
            return False

# miCoche = Coche()
# print(miCoche.arrancar(True))
# miCoche.estado()
# print("------------------------------ A continuacion creamos el segundo objeto -------------------------------")
# miCoche = Coche()
# print(miCoche.arrancar(False))
# miCoche.estado()

# ---------------------------------------------------------------------------------------------------------------------
class Perro:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def setAge(self, ageNew):
        self.__age = ageNew

    def ladrar(self, a):
        print(a)

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

p = Perro("titi", 3)
print(p.getAge())
p.setAge(6)
print(p.getAge())
p.ladrar("Hola")




