
from math import cos,radians,sin,pow,asin,sqrt

def distance(lat1, long1, lat2, long2):
    """ Conociendo el punto exacto de ubicación de cada aeropuerto, puedo calcular la distancia entre ellos
    """
    radius = 6371  # radius of the earth in km, roughly https://en.wikipedia.org/wiki/Earth_radius

    # Lat,long are in degrees but we need radians
    lat1 = radians(lat1)
    lat2 = radians(lat2)
    long1 = radians(long1)
    long2 = radians(long2)

    dlat = lat2 - lat1
    dlon = long2 - long1

    a = pow(sin(dlat / 2), 2) + cos(lat1) * cos(lat2) * pow(sin(dlon / 2), 2)
    distance = 2 * radius * asin(sqrt(a))

    return distance

class Aeropuerto:
    """
    Mi clase aeropuerto.
    """
    def __init__(self, ident, nombre, pais, latitud = 0, longitud = 0):
        self.__ident = ident
        self.__nombre = nombre
        self.__pais = pais
        self.__latitud = latitud
        self.__longitud = longitud

    def cambiarCoordenadas(self, latitud, longitud):
        self.__latitud = latitud
        self.__longitud = longitud

    def getNombre(self):
        return self.__nombre

    def getId(self):
        return self.__ident

    def __repr__(self):
        # return str(self.__ident) + " - " + self.__nombre + " - " + self.__pais
        return "%d | %s | %s | %f | %f" %(self.__ident, self.__nombre, self.__pais, self.__latitud, self.__longitud)

    def distancia(self, aero2):
        return distance(self.__latitud, self.__longitud, aero2.__latitud, aero2.__longitud)

if __name__ == "__main__":
    ae1 = Aeropuerto(507, 'Heathrow', 'United Kingdom')
    ae2 = Aeropuerto(30, 'Campbell River', 'Canada')

    ae1.cambiarCoordenadas(10, -25.3)
    ae2.cambiarCoordenadas(100, 100)

    print(ae1)
    print(ae2)
    print(ae1.distancia(ae2))
    print(ae2.distancia(ae1))