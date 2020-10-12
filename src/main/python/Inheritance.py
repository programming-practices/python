
# Herencia
    # En un lenguaje orientado a objetos cuando hacemos que una clase (subclase) herede de otra clase (superclase) estamos
    # haciendo que la subclase contenga todos los atributos y methodos que tiene la superclase.
    # Python permite que una clase que herede de otra(s) puede sobreescribir cualquier methodo de su(s) clase(s) base,
    # y un methodo puede llamar al methodo de la clase base con el mismo nombre.
    # Es una manera de reutilizar codigo y abstraer al programador de la implementacion que subyace.


# Python permite herencia multiple
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
        # Tambien es posible usar conesta manera, pero esto viene de los versiones antiguas 2.5 2.6 2.7
        # Vehiculo.__init__(self, marca, modelo)
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

# Chtobu ynasledovatsa ot klassa nado perdat eho imia klasu nasledniky v duwki, kak pokazno nize
class Moto(Vehiculo):
    haciendoCaballito = ""
    def caballito(self):
        self.haciendoCaballito = "Voy haciendo el caballito"

    # Aqui nosotros sobre escribimos el metodo de clase iredado Vehiculo.estado
    def estado(self):
        print("Marca:", self.marca, "\nModelo:", self.modelo, "\nEn marcha:", self.enmarcha,
              "\nAcelerado:", self.acelerar, "\nFrerenado:", self.frenar, "\n", self.haciendoCaballito)

# En Python se permite herencia multiple
# Ocurre siguente cosa, es que cuando hay herencia multiple se da preferencia simpre a la primera clase que indique en
# la herencia multiple, en nuestro caso es VuhiculoElectrico. Cuando nosotros vamos crear un objeto de BicicletaElectrica
# en constructor no tenemos que pasar parametros, porque BicicletaElectrica erede el constructor de VehiculoElectrico y
# este constructor no recibe parametros.
class BicicletaElectrica(VuhiculoElectrico, Vehiculo):
    pass

# miMoto = Moto("Honda", "CDR")
# miMoto.caballito()
# miMoto.estado()
# print("------------------------------------------")
# miFurgoneta = Furgoneta("Renault", "Kango")
# miFurgoneta.arrancar()
# miFurgoneta.estado()
# print(miFurgoneta.carga(True))
# print("-------------------------------------------")
# miBicicletaElectrica = BicicletaElectrica("BiciElectrico", "T1000")
# miBicicletaElectrica.estado()

#-----------------------------------------------------------------------------------------------------------------------
class Persona():
    def __init__(self, nombre, edad, Lugar_residencia):
        self.nombre = nombre
        self.edad = edad
        self.lugar_Residencia = Lugar_residencia

    def descripcion(self):
        print("Nombre:", self.nombre, "\nEdad:", self.edad, "\nResidencia:", self.lugar_Residencia)

class Empleado(Persona):
    def __init__(self, nombre_Empleado, edad_Empleado, residencia_Empleado, salario, antiguedad):
        # Aqui nos pasamos parametros al constructor de la clase Person
        super().__init__(nombre_Empleado, edad_Empleado, residencia_Empleado)
        self.salario = salario
        self.antuguedad = antiguedad

    # Otra manera de sobre escribir el methodo de clase Person
    def descripcion(self):
        super().descripcion()
        print("Salario:", self.salario, "\nAntiguedad:", self.antuguedad)

# Antonio = Persona("Antonio", 55, "Espania")
# Antonio.descripcion()
# print("isinstance(Antonio, Empleado) -->", isinstance(Antonio, Empleado))
# print("isinstance(Antonio, Persona) -->", isinstance(Antonio, Persona))
# print("-------------------------------")
# TypeError: __init__() takes 3 positional arguments but 4 were given
# Carlos = Empleado("Carlos", 40, "Espania")
# print("-------------------------------")
# AttributeError: 'Empleado' object has no attribute 'nombre'
# Ana = Empleado(37000, 2006)
# Ana.descripcion()
# print("-------------------------------")
# Pedro = Empleado("Pedro", 46, "Espana", 38000, 2008)
# Pedro.descripcion()
# print("isinstance(Pedro, Empleado) -->", isinstance(Pedro, Empleado))
# print("isinstance(Pedro, Persona) -->", isinstance(Pedro, Persona))

