

class Empleado:
    """
    Clase que representa Empleado de Aeropuerto
    """
    def __init__(self, dni, nombre, tipo, salario):
        self.__dni = dni
        self.__nombre = nombre
        self.__tipo = tipo
        self.__salario = salario

    def __repr__(self):
        return 'Dni: ' + str(self.__dni) + \
               ' - Nombre: ' + str(self.__nombre) + \
               ' - Salario: ' + str(self.__salario)

    def getDNI(self):
        """
        Devuelve el DNI de un empleado.
        """
        return self.__dni

    def getSalario(self):
        """
        Devuelve el salario del empleado.
        """
        return self.__salario

    def setSalario(self, newSalario):
        """
        Modifica el salario del empleado. Recibe un float como argumento que representa
        el salario y modifica el salario del empleado.
        """
        self.__salario = newSalario

class ColeccionEmpleados:
    """
    Clase para almacenar coleccion de Empleados
    """
    def __init__(self):
        self.__elementos = {}

    def __repr__(self):
        txt = ''
        for i in self.__elementos.values():
            txt = txt + str(repr(i)) + "\n"
        return txt

    def __len__(self):
        """
        Devuelve cantidad de empleados
        """
        return len(self.__elementos)

    def alta(self, empleado):
        """
        Permita anadir un empleado a la coleccion de empleados
        """
        if empleado.getDNI() in self.__elementos.keys():
            print("Empleado con este DNI =  %s ya existe en coleccion!!!" %empleado.getDNI())
        else:
            self.__elementos[empleado.getDNI()] = empleado

    def baja(self, empleado):
        """
        Permita eliminar un empleado a la coleccion de empleados.
        """
        if empleado.getDNI() in self.__elementos.keys():
            self.__elementos.pop(empleado.getDNI())
        else:
            print("Empleado con DNI %s no se encuntra en la coleccion de Empleados. "
                  "Y por esta causa no puede dar de baja!!!" %empleado.getDNI)

    def modificarEmpleado(self, DNI, newSalario):
        """
        Permita modificar el salario de un empleado de la lista de empleados. El metodo recibe como
        argumentos el dni de un empleado y el nuevo salario. Si el dni no se corresponde con un
        empleado de la lista de empleados, esta funcion no tiene ningun efecto.
        """
        if DNI in self.__elementos.keys():
            self.__elementos[DNI].setSalario(newSalario)
        else:
            # pass
            print("Empleado con DNI = %s no existe. Y no es posible modificar salario!!!" %DNI)

    def getEmpleados(self):
        """
        Devuelve el dicionario con empleados.
        """
        return self.__elementos


if __name__ == '__main__':
    print('------Prueba  Empleados ----')
    emp1 = Empleado('7894574N', 'Antonio', 'A', 8000)
    emp2 = Empleado('898898R', 'Ana', 'B', 1000)
    # emp3 = Empleado('898898R', 'Ana', 'B', 1000)
    emp1.setSalario(9000)
    print(emp1)
    print(emp2)
    # print(emp3)
    print('Dni: ', emp1.getDNI())
    # print('Dni: ', emp2.getDNI())
    # print('Dni: ', emp3.getDNI())
    print('------ Prueba Coleccion de empleados ----')
    coleccionE = ColeccionEmpleados()
    coleccionE.alta(emp1)
    coleccionE.alta(emp2)
    # coleccionE.alta(emp3)
    coleccionE.modificarEmpleado(emp1.getDNI(), 8888888)
    print(coleccionE)
    print(type(coleccionE.getEmpleados()))
