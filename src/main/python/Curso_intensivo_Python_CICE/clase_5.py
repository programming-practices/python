
# ---------------------------------------------------- Ejercicio 0 -----------------------------------------------------
"""
Definiendo dos listas de igual longitud, una para nombres, y otra para notas,
rellenar un diccionario cuyas claves sean los nombres y las notas sean los valores
del mismo.

"""
# 1. Voy a usar dos listas cualesquiera. Es mas facil si ambas son de la misma
# longitud. Las asigno a variables de nombres de relevantes.

lista_nombres = ["Ãlvaro", "Jorge", "Pedro", "Sara", "Ana"]
lista_notas = [7, 8, 8, 4, 7]

# Lo que busco es pasar de tener un diccionario vacio a uno que tenga:
# Alvaro: 7, Jorge:8, Pedro:0 y asÃ­... correlacionando la primera posicion de
# cada lista.

# Primero defino un diccionario vacio:

dic = {}  # recordemos que el nombre que le doy a la variable es arbitrario,
# con que me sirva para acordarme de que va, me vale.

# ahora voy a tener que rellenar el diccionario, voy a repasar como se
# introduce un valor en el mismo:
# dic[key] = value

# ahora, intentaremos hacerlo de modo programÃ¡tico, usando un bucle.
# se puede hacer con ambos tipos, pero sale mucho mejor con while

i = 0
while i < len(lista_nombres):  # da igual que lista coja, ambas son igual de largas
        dic[lista_nombres[i]] = lista_notas[i]
        i += 1  # que no se os olvide esto!!!

# FIN


# NOTAS:
# quiero recordar que para obtener datos de una lista (no diccionarios),
# vale con nombrar la lista y poner el indice entre corchetes:
# lista_nombres[0] da el primer valor de la lista_nombres, que es Alvaro.
# Asi, dentro del bucle, usamos lista_nombres[i] para obtener cada posicion de esa lista
# y usamos lista_notas[i] para obtener el valor de esa lista en la misma posicion.

# ---------------------------------------------------- Ejercicio 1 -----------------------------------------------------
"""
Enunciado:
1. Se va a facilitar una lista de numeros. El objetivo es ordenar sus elementos de mayor a menor, eliminando aquellos
   que estén repetidos, por último habrá que ir metiendo los resultados en una lista nueva.

2. En este caso, se va a facilitar una lista de strings. El objetivo es ordenarlos por longitud, de mayor a menor.
   Aquí no habrá repetidos

3. Convertir el programa anterior en una función.
"""


numeros = [3,5,2,6,7,7,2,1,3,6,8,9,2,3,1]
palabras = ["maldito duende","hay poco rocknroll", "la chispa adecuada", "sirena varada", "malas intenciones", "entre dos tierras"]

sortList = sorted(numeros)
resultList = []
for num in sortList:
        # print(resultList.__contains__(num))
        if resultList.__contains__(num):
                pass
        else:
                resultList.append(num)
print(resultList)

# ---------------------------------------------------- Exercicio 2 -----------------------------------------------------
"""
Enunciado:
1. Voy a recibir un diccionario que contiene los nombres de los alumnos de mi clase y la nota que han obtenido. Mi objetivo 
   será mandar un email a cada uno de ellos con su nota. Como aún no sé mandar emails con python, de momento solo voy a 
   crear el cuerpo del texto. El objetivo es imprimir por pantalla, usando un loop, el siguiente cuerpo del mensaje:
   “Alejandro ha sacado un 10”, cambiando en cada caso, el nombre del alumno para uno de los que aparece en el diccionario 
   y la nota por la que corresponde a cada alumnos

2. Convertir el paso anterior en una funcion
"""
alumnos = {
        "Alberto":9,
        "Chema":8,
        "David":10,
        "Andrés": 5,
        "Lucía":9,
        "Elena":6,
        "Sandra": 4,
        "Julio": 6,
        "Jorge":8,
        "Bea":7
        }
# ------------------------------------------------------ Ejercicio 3 ---------------------------------------------------
"""

"""
import smtplib

me = input('meter mi email aqui: ')
passw = input('meter mi pass: ')
destino = input('meter el email del destinatario final: ')
destino_cc = input('meter email en copia: ')
asunto = input('meter el asunto del email: ')
mensjae = input('cuerpo del email: ')

server = smtplib.SMTP(smtpserver)


def sendemail(from_addr, to_addr_list, cc_addr_list, subject, message, login, password,
              smtpserver='smtp.gmail.com:587'):
        header = f'From: {from_addr}'
        header += f'To: {to_addr_list}'
        header += f'Cc: {cc_addr_list}'
        header += f'Subject:{subject}'
        message = header + message

        server = smtplib.SMTP(smtpserver)
        server.starttls()
        server.login(me, passw)
        server.sendmail(from_addr, to_addr_list, message)
        server.quit()


sendemail(me, destino, destino_cc, asunto, mensaje, me, passw)

# ------------------------------------------------------ Ejercicio 4 ---------------------------------------------------
"""
Crear un archivo que solo contenga una clase. Dicha clase se llamará Circulo (o Circle), y deberá recibir el radio cuando 
se instancie (recordemos que instanciar es crear un objeto de esa clase). El radio será uno de los atributos. Como 
métodos, el circulo tendrá devolver el perímetro (y guardarlo como atributo), devovler el área (y guardarla como atributo) 
y por último, escalar el circulo (aumentar su radio y después su area y su perímetro, para que no queden descolgados).
"""
# ------------------------------------------------------ Ejercicio 5 ---------------------------------------------------
# ------------------------------------------------------ Ejercicio 6 ---------------------------------------------------