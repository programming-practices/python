

def menu():
    print('----- Gestión de aeropuertos ------')
    print('-----------------------------------')
    print()
    print('1. Cargar pilotos.')
    print('2. Cargar aeropuertos.')
    print()
    print('3. Listar pilotos')
    print('4. Listar aeropuertos.')
    print('5. Listar rutas.')
    print()
    print('6. Modificar salario de un piloto')
    print('7. Crear nueva ruta')
    print('8. Guardar todas las rutas')
    print()
    print('0. Salir')


def run():
    seguir = True
    rutas = {}
    datos = bd.BaseDeDatos()
    while seguir:

        menu()
        opcion = int (input('Elige una opción: '))
        if opcion == 0:
            despedida()
            seguir = False

        elif opcion == 1:
            opcionCargaPilotos(datos)

        elif opcion == 2:
            opcionCargaAeropuertos(datos)

        elif opcion == 3:
            opcionListadoPilotos(datos)

        elif opcion == 4:
            opcionListadoAeropuertos(datos)

        elif opcion == 5:
            opcionListadoRutas(rutas)

        elif opcion == 6:
            dni = str (input('Introduce dni del empleado: '))
            sala = int (input('Introduce el nuevo salario: '))
            datos.modificarPiloto(dni, salario = sala)

        elif opcion == 7:
            opcionCrearNuevaRuta(datos, rutas)

        elif opcion == 8:
            opcionGuardarRutas(rutas)

        else:
             pass