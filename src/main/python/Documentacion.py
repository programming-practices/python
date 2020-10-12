
class Fecha:
    """
    Este clase esta echo para specificar la fecha
    """
    def __init__(self, aFecha):
        self.__fecha = aFecha

    def getFecha(self):
        """
        Este methodo esta dedicado par devolver la __fecha
        :return: int
        """
        return self.__fecha

    def setFecha(self, newFecha):
        """
        Este methodo esta dedicado para cambiar la fecha actual al valor newFecha
        :param newFecha: int
        :return: None
        """
        self.__fecha = newFecha

miFecha = Fecha(23)
print(miFecha.getFecha())
miFecha.setFecha(45)
print(miFecha.getFecha())
