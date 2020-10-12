#-------------------------------------------- Ejercicion 1
# Supongamos que tenemos un fichero de texto encuensta con los datos de una encuesta realizada por un agricultor de rabanos.
# Dicho fichero recoge informacion de las pereferencias de los consumidores acerca de las distintas variedades.
    # Cada linea del fichero tiene el siguente formato:
    # nombre_cliente - variedad_de_rabano

# El fichero dispone de casi 700 opciones de usuarios. Abre el fichero para ver el contenido.
    # Descargate el fichero encuesta en tu directorio de trabajo
    # Abrelo con instrucion open
    # Realiza un print de las 10 primeras lineas del fichero
    # Utiliza un bucle for de 10 iteraciones para leer el contenido del fichero.
fichero_radishsurvey = open("/home/dtrl/GitHub/LessonsPython/src/main/resources/radishsurvey.txt")
# for i in range(10):
#     print(fichero_radishsurvey.readline())

#-------------------------------------------- Ejercicio 2
# Escribe una funcion llamada clientes() que devuelva la lista de clientes que han votado por alguna variedad de rabanos:
    # Utiliza un bucle for para leer el contenido completo de fichero.
    # Usa la funcion strip() para eliminar los saltos de linea.
    # Usa la funcion split para separar el nombre del cliente y la variedad de rabanos
    # Utiloza la funcion append para anadir el nombre del cliente a una lista de clientes (previamente inicializada).
    # No te olvides de realizar un return para devolver el resultado.
# Nota: El cliente numero 15 en la lista es "Jonathan Rolph".
# print(type(fichero_radishsurvey))
# listaDeClientes = fichero_radishsurvey.readlines()
# print(clientes_S)
# def clientes(listaClientes):
#     lC = []
#     for cliente in listaClientes:
#         temp = cliente.strip().split(' -')
#         lC.append(temp[0].title())
#     return lC
# todosClisentes = clientes(listaDeClientes)
# print(todosClisentes[15])

#---------------------------------------------- Ejercicio 3
# El agricultor desea conocer el numero total de votos que ha recibido la variedad de rabanos 'White Icicle'. Define una
# funcion denominada votosWI() que calcula el dato pedido.
    # Utiliza una vriable entera inicializada a 0 para almacenar el contador de votos.
    # Utiliza una bucle for para leer contenido del fichero.
    # Usa la funcion split para separar el nombre del cliente y la variedad de rabano.
    # Usa la instrucion if para comprobar si la variedad de rabano es 'White Icicle'. En caso afirmativo suma 1 al
    # contador de votos.
    # No te olvides de devolver el numero de votos mediante la instruccion return.
    # Nota: El resultado es 59 votas.

# def votosWI(lista):
#     countVotos = 0
#     for linea in lista:
#         (cliente, voto) = linea.split(' - ')
#         voto = voto.strip()
#         if voto.strip().title() == 'White Icicle'.title():
#             # print(voto)
#             countVotos = countVotos + 1
#     return countVotos
# print(votosWI(list(fichero_radishsurvey)))

#------------------------------------------------- Ejercicio 4
# Generaliza la funcion anterior y define una funcion que calcule el numero de votos que ha recebido una variedad
# cualquiera de rabanos.
# Define una funcion llamada votos() que reciba como parametro una variedad de rabano y devuelva la cantidad de votos.
# Nota: La variedad 'Snow Belle' ha recebido 58 votos.

# rabanoV = 'Snow Belle'
# def votos(lista, rabano):
#     countVotos = 0
#     for linea in lista:
#         (cliente, voto) = linea.split(' - ')
#         voto = voto.strip()
#         if voto.strip().title() == rabano.title():
#             print(voto)
#             countVotos = countVotos + 1
#     return countVotos
# print(votos(list(fichero_radishsurvey), rabanoV))

# ------------------------------------------------- Ejercicio 5
# Define una funcion llamada clientesPorVariedad que recibe como parametro una variedad de rabano y devuelve la lista de
# clientes que han votado por esa variedad. Ten en cuenta que esta funcion es casi indentica que la interior.
# Nota: Prueba con la variedad de rabano 'White Icicle'.

# rabanoV = 'Snow Belle'
# rabanoV = 'White Icicle'
# def clientesPorVariedad(lista, rabano):
#     listaDeClientes = []
#     for linea in lista:
#         (cliente, voto) = linea.split(' - ')
#         voto = voto.strip()
#         if voto.strip().title() == rabano.title():
#             print(voto)
#             listaDeClientes.append(cliente.strip().title())
#     return listaDeClientes
# print(clientesPorVariedad(list(fichero_radishsurvey), rabanoV))

#--------------------------------------------------- Ejercicio 6
# Al agricultor le gusta conocer el numero de votos recibidos por cada variedad.Define una funcion llamada votos_por_variedad()
# que devuelve la informacion del numero de votos por variedad. Usa un dicionario para almacenar esa informacion. La clave
# del diccionario es la variedad y el valor es un entero que representa el numero de votos.
    # Crea un diccionario vacio
    # Utiliza un bucle for para leer el contenido del fochero.
    # Usa la funcion strip para eliminar saltos de linea.
    # Usa la funcion split para separar el nombre del cliente y la variedad de rabano.
    # Usa la instruccio if para comprobar si la variedad esta en el diccionario. En caso afirmativo suma 1  al valor. En
    # caso contrario anade una nueva variedad al diccionario.
    # No te olvides de devolver diccionario pedido mediante la instruccion return.
# Observa la solucion. Si te das cuenta, en el diccionario aprecen variedades con miniscula mayuscula. Tambien aparecen
# variedades con espacios en blanco al principio. Un desastre de datos.
# Tenemos que hacer una limpieza de datos para solventar el problema anterior.
    # Corige la funcion anterior haciendo uso de la funcion strip() y title() en cada variedad de rabanos.
# Por aun sale cosas raras. Fijate en las variedades 'Sicily Giant' y 'Sicily  Giant'. Deberia ser la misma variedad.
# Usa el methodo replace() para sustituir las apariciones de dos espacios en blanco por un solo espacio en blanco.
def clientesPorVariedad(lista):
    dicVotosPorRabanos = {}
    for linea in lista:
        (cliente, rabano) = linea.split(' - ')
        rabano = rabano.strip().title().replace('  ', ' ')
        if rabano in dicVotosPorRabanos.keys():
            dicVotosPorRabanos[rabano] = dicVotosPorRabanos[rabano] + 1
        else:
            dicVotosPorRabanos[rabano] = 1
    return dicVotosPorRabanos
# print(clientesPorVariedad(list(fichero_radishsurvey)))

#------------------------------------------------- Ejercicio 7
#El agricultor desea guardar en un fichero de texto la lista de las variedades junto con el numero de votos obenidos.
    # Abre un fichero llamado 'resultado.txt' en modo escritura
    # Invoca la funcion 'voto_por_variedad() para obtener el diccionario que contiene el numero de votos por variedad
    # Utiliza la instruccion for para iterar sobre los elementos del diccionario y escribir en el fichero.
    # Cierra el fichero.
ficheroResultado = open('/home/dtrl/GitHub/LessonsPython/src/main/resources/resultado.txt', 'w')
dicionarioV = clientesPorVariedad(list(fichero_radishsurvey))
for variedad in dicionarioV.keys():
    ficheroResultado.write('%s --> %d\n' %(variedad, dicionarioV[variedad]) )
ficheroResultado.close()

fichero_radishsurvey.close()
