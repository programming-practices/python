# name = "vasya pupkin"
# print(name.title())
# print(name)

# Se pueden encerrar en comillas doble o similar
# objetivo = "Aprender a manejar Python"
# meta = 'Ser todo un experto'
# print(objetivo)
# print(meta)

# Las cadenas de caracteres se pueden concatenar con el operador +
# a = 'Anna'
# b = 'Me he namorado de ' + a
# print(b)

# Tambien podemos multiplicar una cadena por un numero
# print(a * 4)

# Para conoser longitud de una cadena, se utilisa la finccion len
# print('Longitud de ', a, len(a))

# Las cadenas largas de caracteres se encieren entre triple comilla double y pueden incluir saltos de linea
# txt =   """                                         Where does it come from?
#         Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical
#         Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at
#         Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from
#         a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the
#         undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum"
#         (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of
#         ethics, very popular during the Renaissance. The first line of Lorem Ipsum, "Lorem ipsum dolor sit amet..",
#         comes from a line in section 1.10.32.
#
#         The standard chunk of Lorem Ipsum used since the 1500s is reproduced below for those interested. Sections 1.10.32
#         and 1.10.33 from "de Finibus Bonorum et Malorum" by Cicero are also reproduced in their exact original form,
#         accompanied by English versions from the 1914 translation by H. Rackham."""
# print(txt)

mensaje = """Esto es mensaje
de tres saltos
en la linea"""
# print(mensaje)

# Hay caracteres que debemos escapar para que aparezcan, como las comillas
# especial = "Las \"comillas\" son caracteres especiales"
# print(especial)

# Podemos producir un salto de linia con \n
# especial = "Hay ortos caracters especiales como el salto de linea.\nServe para representar el fin de linea en ficheros."
# print(especial)
# Numero de characteres en string
# print(len(especial))

# bara devirtida robut tak wcho polychaetsa salto de linea en el codigo, ce vukorustovuetsa napruklad dlya toho wchobu ne
# pusatu vse v odnii linii a mozno perenesti na dryhy liniy
especial = "Hay ortos caracters especiales como el salto de linea.\
Serve para representar el fin de linea en ficheros."
# print(especial)

# Las cadenas son consideradas como una seccuencia de caracteres y por tanto pueden ser tratadas como tuplas o listas.
a = "Ana"
# print(a, a[0], a[2])

"""Los strings son inmutales, no se pueden modificar un string sin crear otro nuevo."""
mensaje = "Vaya se escribe con v"
b = mensaje.replace('V', 'v')
# print(b, mensaje)


#--------------------------------------------- Dar formato a un string -------------------------------------------------
# Si queremos mostrar por pantalla una variable que va cambiando(por ejemplo, cundo recorremos una coleccion con un bucle),
# debemos dar un formato al mensaje al mostrar. El operator % permite construir strings reemplazar partes de la cadena con
# los datos guardados en variables. Cuando se amplia a enteros, % es el operator modulo pero cuando es un string, % es el
# operator de formato
# Por ejemplo, %d significa que el segundo operador debe formatearse como un entero (d quiere decir decimal)
tall = 42
# print("Tengo una talla %d." %tall)

# Ademas, se puede usar %f para mostrar numeros de coma flotante y %s para mostrar strings
# print("En %d meses quiero pasar %.2f %s menos." %(3, 2.505, 'kilos'))
# A esta manera de dar formato a un string se la llama old style

# for i in range(5):
#     print(f'valor de la variable {i}')

# -------------------------------------------- New Style de dar formato ------------------------------------------------
# En la PEP 3101 se propuso una nueva forma de dar formato a los strings, llamada a la funccion formato()
# str.format(<variable>, <variable>...)
string = "The sum of 1 + 2 is {0}".format(1 + 2)
# print(string)

string = "Si 1 kg de tomates cuesta {0} Euros, un cuarto de kg cuesta {1:.2f}".format(5, 5/3)
# print(string)

# Segun la documentacion oficial de Python:
    # Este metodo de formateo de string es el nuevo estandart de Python 3 y deberia ser preferido frente al formato % en
    # el codigo nuevo.

# print("La suma de {0} y {1} es igual {2}".format(2, 5, 7))
# El llava uno no esta usando
# print("La suma de {0} y {0} es igual {2}".format(2, 5, 4))

# -------------------------------------------------- Methodos de cadena ------------------------------------------------
valueStr = " Hola. Como estas? "
valueInt = '3'
print(valueStr.lower())
print(valueStr.upper())
print(valueStr.capitalize())
print(valueStr.count('a'))
print(valueStr.find("a"))
print(valueStr.isdigit())
print(valueInt.isdigit())
print(str.isalnum(valueStr))
print(str.isalpha(valueStr))
print(valueStr.split())
print(valueStr.strip())
print(valueStr.rfind('a'))
print(valueStr.replace('a', 'r'))
