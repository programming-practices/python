
# Excepciones, que son?
    # Las exceptiones son errores que ocurren durante la ejecucion del programa. La sintaxis del codigo es corecta pero
    # durante la execucion ha ocurrido "algo inesperado".
    # Este tipo de errores de ejecucion se pueden controlar para que la ejecucion del programa continue. Es lo que se
    # conoce como manejo o control de excepciones.

# Bloqeu true tiene que tener un except o un finally
# Las exceptiones son un tipo de error que aparecen durante la ejecucion del programa.
# Pueden producirse por un uso icorrecto del programa por parte del usuario. Por ejemplo si el usuario introduce una cadena
# cuando se espera un numero.
# En otras ocasiones pueden deberse a errores de programacion. Por ejemplo, si una funcion interna acceder a la quinta
# posicion de una lista de 3 elementos o realizar una division por cero.

#------------------------------------------------ Prueba Exception -----------------------------------------------------
# Cuando ocurre una exception, puede tener un valor asociado, tambien conocido como el argumento de la exception. En el
# codigo anteriror, el argumento de exception es la cadena 'Radio Negativo'.
# La presencia y el tipo de argumento depende del tipo de exception.
# except puede especificar una variable justo despues del nombre de exception. La variable se vincula a una instancia de
# exception con los argumentos almacenados en instance.args.
# try:
#         print(3 / 0)
# except ZeroDivisionError as ne:
#         print(ne.args)
#         print('Se ha producido una error: ' + ne.args[0])

# try:
#         print(3/0)
# except:
#         print("Error. Se captura cualquier exception!!!")


def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multiplica(num1, num2):
    return num1 * num2

def divide(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("No se puede dividir entre 0")
        return "Operacion erronea"
# while True:
#     try:
#         op1 = (int(input("Introduce el primer número: ")))
#         op2 = (int(input("Introduce el segundo número: ")))
#         break
#     except ValueError:
#         print("Valores introducidos no son correctos. Intentalo de nuevo!!!")

# operacion = input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")
#
# if operacion == "suma":
#     print(suma(op1, op2))
# elif operacion == "resta":
#     print(resta(op1, op2))
# elif operacion == "multiplica":
#     print(multiplica(op1, op2))
# elif operacion == "divide":
#     print(divide(op1, op2))
# else:
#     print("Operación no contemplada")
#
# print("Operación ejecutada. Continuación de ejecúción del programa ")

#-----------------------------------------------------------------------------------------------------------------------
def divide():
    try:
        op1 = (float(input("Introduce el primero numero: ")))
        op2 = (float(input("Introduce el segundo numero: ")))
        print("La division es: ", op1/op2)
    except ZeroDivisionError:
        print("No se puede devidir entre 0 !!!")
    except ValueError:
        print("El valor inproducido es erroneo!!!")
    print("Calculo finalizado")

def divide2():
    try:
        op1 = (float(input("Introduce el primero numero: ")))
        op2 = (float(input("Introduce el segundo numero: ")))
        print("La division es: ", op1/op2)
    except:  # Asi se capturan todas exceptiones, es no recomendable programar asi.
        print("Ha ocurrido una error!!!")
    print("Calculo finalizado")

def divide3():
    try:
        op1 = (float(input("Introduce el primero numero: ")))
        op2 = (float(input("Introduce el segundo numero: ")))
        print("La division es: ", op1/op2)
    except ZeroDivisionError:
        print("No se puede devidir entre 0 !!!")
    except ValueError:
        print("El valor inproducido es erroneo!!!")
    finally:
        print("Calculo finalizado")
#---------------------------------------------- Lansar excepiones ------------------------------------------------------
def evaluaEdad(edad):
    if(edad < 0):
        # Con palabra reservada raise se puede lansar exception
        raise TypeError("No se permiten edades negativas")
        raise NameError("No se permiten edades negativas")

    if(edad < 20):
        return "Eres muy joven"
    elif(edad < 40):
        return "Eres joven"
    elif(edad < 65):
        return "Eres maduro"
    elif(edad < 100):
        return "Cuidate..."

# print(evaluaEdad(-15))

import math
def calculaRaiz(num):
    if(num < 0):
        raise ValueError("El numero no puede se negativo")
    else:
        return math.sqrt(num)
# value = int(input("Introduce un numero:"))
# try:
#     print(calculaRaiz(value))
# except ValueError as ErrorDeNumeroNegativo:  # Con palabra reservada as se puede dar un nombre o un alias a ese error
#     print(ErrorDeNumeroNegativo)             # que va adelante de palabra reservada as
# print("Programa terminada")



# divide()
# divide2()

# a = 1 / 0
# print(a)
# b = 0 / 1
# print(b)