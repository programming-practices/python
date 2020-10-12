import aeropuertos as aero

class ColeccionAeropuertos:
    """
    Clase para almacenar coleccion de Aeropuertos
    """
    def __init__(self):
        """
        Inicializa la coleccion
        """
        self.__elementos = {}
        self.__contador = 0

    def __repr__(self):
        """
        Devuelve u na cadena de caracteres que contiene la información de todos los aeropuertos
        en el diccionario __elementos__.
        """
        txt = ''
        for i in self.__elementos.values():
            txt = txt + str(repr(i)) + "\n"
        return txt

    def __len__(self):
        """
        Devuelve cantidad de aeropuertos.
        """
        return len(self.__elementos)

    def alta(self, aeropuerto):
        """
        Permita añadir un aeropuero a la colección de aeropuertos.
        """
        if aeropuerto.getId() in self.__elementos.keys():
            print("El aeropuerto con este ID = %s ya existe en coleccion de aerouertos. "
                  "Aeroouerto guardado en la coleccion con este ID "
                  "es \"%s\"" %(aeropuerto.getId(), self.__elementos[aeropuerto.getId()]))
        else:
            self.__elementos [aeropuerto.getId()] = aeropuerto

    def baja(self, idAeropuerto):
        """
        Permita eliminar un aeropuerto de la colección de aeropuertos.
        """
        if idAeropuerto in self.__elementos.keys():
            self.__elementos.pop(idAeropuerto)
        else:
            print("Aeropuerto con este ID = %d no existe, y por esta causa es imposible dar la baja!!! " %idAeropuerto)

    def getAeropuerto(self, idAeropuerto):
        """
        Reciba como argumento el identificador de aeropuerto y devuelva un aeropuerto
        (objeto de la clase Aeropuerto).
        """
        # return self.__elementos[idAeropuerto]      # si no existe elemento sale error
        return self.__elementos.get(idAeropuerto)  # si no existe elemento devuelve None




if __name__ == '__main__':

    ae1 = aero.Aeropuerto(507,'Heathrow', 'United Kingdom' )
    ae2 = aero.Aeropuerto(30,'Campbell River' , 'Canada', 10)
    ae3 = aero.Aeropuerto(30,'River' , 'Canada', 10)
    ae4 = aero.Aeropuerto(333,'River ere' , 'Canada fr', 101)

    col = ColeccionAeropuertos()
    col.alta(ae1)
    col.alta(ae2)
    col.alta(ae3)
    col.alta(ae4)
    print('------------------')
    print(col.getAeropuerto(507))
    col.baja(31)
    print(col)