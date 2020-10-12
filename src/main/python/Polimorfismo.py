
class Coche():
    def desplazamiento(self):
        print("Me desplazo utilisando chuatro ruedas")

class Moto():
    def desplazamiento(self):
        print("Me desplazo utilisando dos ruedas")

class Camion():
    def desplazamiento(self):
        print("Me desplazo utilisando seis ruedas")

def dezplasaminetoVehiculo(vehiculo):
    vehiculo.desplazamiento()

miVehiculo = Camion()
dezplasaminetoVehiculo(miVehiculo)