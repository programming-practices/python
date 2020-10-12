
import bdAeropuertos as aerCA
import aeropuertos as aer
import bdEmpleados as emp

class BaseDeDatos:
    """
    Base de datos para aeropuertos y pilotos
    """
    def __init__(self):
        self.__aeropuertos = aerCA.ColeccionAeropuertos()
        self.__pilotos = emp.ColeccionEmpleados()

    def loadAeropuertos(self, path):
        """
        Dado un fichero de tipo .txt, permita leer todos los aeropuertos de un fichero y añadirlos
        a la colección de aeropuertos.
        """
        try:
            openFile = open(path)
            for line in openFile.readlines():
                word = line.split(',')
                aeropuerto = aer.Aeropuerto(int(word[0].rstrip().strip().title().replace('\"', '')),
                                            str(word[1].rstrip().strip().title().replace('\"', '')),
                                            str(word[3].rstrip().strip().title().replace('\"', '')),
                                            float(word[6].rstrip().strip().title().replace('\"', '')),
                                            float(word[7].rstrip().strip().title().replace('\"', '')))
                self.__aeropuertos.alta(aeropuerto)
        except:
            print("Error") # No megusta
        finally:
            openFile.close()

    def loadEmpleados(self, path):
        """
        Dado un fichero de tipo .txt, permita leer todos los empleados de un fichero y añadirlos
        a la colección de pilotos.
        """
        try:
            openFile = open(path)
            for line in openFile.readlines():
                lineSplit = line.split(',')
                dni = lineSplit[0].strip().upper().replace('  ', ' ').rstrip()
                nombre = lineSplit[1].strip().title().replace('  ', ' ').rstrip()
                tipo = lineSplit[2].strip().title().replace('  ', ' ').rstrip()
                salario = lineSplit[3].strip().replace('  ', ' ').rstrip()
                if salario == '':
                    salario = 0.0
                empleado = emp.Empleado(dni, nombre, tipo, salario)
                self.__pilotos.alta(empleado)
        except:
            print("Error")
        finally:
            openFile.close()

    def lenAeropuertos(self):
        """
        Devuelve el número de aeropuertos cargados en la Base de datos.
        """
        return len(self.__aeropuertos)

    def lenPilotos(self):
        """
        Devuelve el número de pilotos cargados en la Base de datos.
        """
        return len(self.__pilotos)

    def listadoPilotos(self):
        """
        Devuelve el listado de los pilotos. Devuelve un objeto de tipo ColeccionEmpleados.
        """
        return self.__pilotos

    def listadoAeropuertos(self):
        """
        Devuelve el listado de los aeropuertos. Devuelve un objeto de tipo ColeccionAeropuertos.
        """
        return self.__aeropuertos

    def getAeropuerto(self, id):
        """
        Devuelve un aeropuerto de la base de datos. Recibe como argumento de entrada un identificador de
        aeropuerto y devuelve un objeto de la clase Aeropuerto.
        """
        return self.__aeropuertos.getAeropuerto(id)

    def modificarPiloto(self, dni, newSalario):
        """
        Permita modificar el salario de un empleado de la base de datos. El método recibe como argumentos
        el dni de un empleado y el nuevo salario. Si el dni no se corresponde con un empleado de la base
        de datos, esta función no tiene ningún efecto.
        """
        # for empleado in self.__pilotos.getEmpleados().values():
        #     if dni == empleado.getDNI():
        #         empleado.setSalario(newSalario)

        self.__pilotos.modificarEmpleado(dni, newSalario)   # or.  esta linea hace menos trabajo

    def getAeropuertos(self):
        """
        Devuelve diccionario de aeropuerto.
        """
        return self.__aeropuertos

if __name__ == '__main__':
    datos = BaseDeDatos()
    datos.loadAeropuertos('/home/dtrl/GitHub/LessonsPython/src/main/resources/airports.txt')
    datos.loadEmpleados('/home/dtrl/GitHub/LessonsPython/src/main/resources/empleados.txt')

    print("--------len-------------")
    print('Pilotos: ',  datos.lenPilotos())                   # +
    print('Aeropuertos: ', datos.lenAeropuertos())

    print('--------getAeropuerto-------')
    print(datos.getAeropuerto(1229))
    # print(datos.getAeropuertos())

    print('--------listado--------------')
    # print(datos.listadoPilotos())
    # print(datos.listadoAeropuertos())

    print('--- Prueba cambio salario -----')
    datos.modificarPiloto('182988P', 7777)                  # +
    print(datos.listadoPilotos())                           # +

# if __name__ == '__main__':
#     baseDeDatos = BaseDeDatos()
#     baseDeDatos.loadEmpleados()
    # print(baseDeDatos.lenPilotos())
    # print(baseDeDatos.listadoPilotos())
    
    # baseDeDatos.loadAeropuertos()
    # print(baseDeDatos.lenAeropuertos())