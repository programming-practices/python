
# Condicionales
    # Swich  ---> no exicsiste en python
    # Concatenacion de operadores de comparacion
    # Operadores logicos "and" y "or"
    # Operador "in"

# Cunado ponemos: al final de la primera linea del condicion, todo lo que vaya a continuacion con un nivel de sangrado
# superior se considera dentro del conditional
# Se puede asignar dos variables ala ves, es decir esto es desempaquetado de tupla 2,0 a x,y es asignado
#x, y = 2, 0
#if x > y:
#    print("x es mayor que y")
#    print("x sigue siendo mayor que y")
# print(x)
# print(y)

# En cuanto escribimos la primera linea con un nivel de sangrado inferior, hemos cerrado el condicional
# if 1 < 0:
#     print("1 es mayor que 0")
# print("Esto se ejecuta siempre")  # esto no esta dentro de bloque if

# Errores de sangrado
    # Los errores de sangrado son comunes, cuando todas las sentencias de un bloque deben dejar el mismo numero de espacio.
# if  1 > 0:
#     print("1 es mayor que 0")
#      print("1 sigue siendo mayor que 0")  # ERROR de sangrado, IndentationError: unexpected indent

# Se prefiere if ... is not a if not ... is:
# Bien
# if algo is not None:
# Mal
# if not algo is None:

# print("Verificacion de acceso")
# edad_usuario = int(input("Introdise tu edad. Por favor!!!\n"))

# if edad_usuario < 18:
    # print("No pudes pasar!!!")
# elif edad_usuario > 120:
#     print("Edad incorecta")
# else:
#     print("Puedes pasar!!!")
# print("Final de programa.")

# edad = -7
# if 0 < edad > 120:
#     print("Edad es correcta")
# else:
#     print("Edad es incorrecta")

# value1 = 2
# value2 = 3
# value3 = 4
# value5 = 5
# value6 = 7
# if value1 < value2 < value3 < value5 < value6:
#     print("Hello")

# Example in
# print("Asignaturasoptativas Ano 2017")
# print("Asignaturasoptativas: Informatica grafica - Pruebas de software - Usabilidad y accesibilidad")
option = input("Escribe la asignatura escogida: ")
asignatura = option.lower()     # Etot method delaet vse bykvu malenkimi
if asignatura in ("informatica grafica", "pruebas de software", "usabilidad y accesibilidad"):
    print("Asignatura elegida " + asignatura)
else:
    print("La asignatura escogida no esta comtemplada")


# ------------------------------------------------- Expresiones Ternarias ----------------------------------------------
# Las expresionesternarioas en Python permiten asignar o evolver un valor con operaciones condicionales en un sola linea:
# Expresiones ternarias se usan solo con condiciones sencillas.
# <variable> = <valorSiTrue> if <condicion> else <valorSiFalse>
# Equivalente a version if else
#if <condicion>:
#   <variable> = <valorSiTrue>
#else:
#   <variable> = <valorSiFalse>
# y = 5
y = 2
x = 'Hola' if y < 4 else 'Adios'
print(x)