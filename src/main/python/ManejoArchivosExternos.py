
# En Python para abrir un fichero usamos la funcion open(), que resibe el nombre del archvo a abrir. Por defecto, si no
# indicamos nada, el fichero se abre en modo lectura.

# Faces neceasrias para guardar informacion en archivo externo
    # Creacion
    # Apertura
    # Manipulation
    # Cierre

# Modo en que nos vamos a abrir el archivo
    # Lectura - para leer archivo
    # Escritura - para crear y escribir contenido recien creado archivo
    # Append - agregar un informacion a un archivo que ya existe y ya que tiene informacion en su enterior

from io import open

# --------------------------------------- Aqui abrimos archivo para lectura --------------------------------------------
# La funcion open() abrira el fichero en el nombre indicado, en este caso el fichero archivoCreadoDesdePython.txt . Si no
# tiene exito, se lansa una exception. Si se ha podido abrir el fichero corectamente, la variable archivo_txt nos permite
# manipularlo.
# archivo_txt = open("/home/dtrl/GitHub/LessonsPython/src/main/resources/archivoCreadoDesdePython.txt")
# archivo_txt = open("/home/dtrl/GitHub/LessonsPython/src/main/resources/archivoCreadoDesdePython.txt", "r")
# archivo_txt = open("/home/dtrl/GitHub/LessonsPython/src/main/python/Inheritance.py", "r")
# textoLeido = archivo_txt.read()
# archivo_txt.close()
# print(textoLeido)

# textoLeidoPorLinea = archivo_txt.readlines()
# archivo_txt.close()
# print(textoLeidoPorLinea)

# print(archivo_txt.read())
# Si nos ponemos otro print con archivo_txt.read() no nos va escribir otra ves contenido de archivo. Es porque el cursor
# de lectura se encuentre en final de contenido de archivo
# print(archivo_txt.read())

# Para mover el cursor tenemos que usar la funcion seek(), si queremos mover cursor al una posicion, tenemos que pasar
# parametro a la funcion seek(28), cursor se va encontrar en la posicion 28 en el archivo. Por ejemplo
# archivo_txt.seek(0)  # con esta funcion nos colocamos el cursor en el primer character de archivo
# print(archivo_txt.read())  # Y ahora nos emprime dos veces el contenido de archivo

# archivo_txt.seek(20)
# print(archivo_txt.read())

# Si pasamos parametro ne el methodo read(), el methodo read() va leer el fichero hasta la posicion que hemos pasado
# por paramero. Por ejemplo
# print(archivo_txt.read(25))  # El cursor se quede ne esta posicin esperando siguente read()
# Si nos segimos leer arcchvo, empezamos leer archivo desde la posicion 25
# print("----------Leer desde la posicion 25-------------------")
# print(archivo_txt.read())

# Para colocar cursor en medio de texto se puede hacer con esta manera
# archivo_txt.seek(len(archivo_txt.read()) / 2)
# print(archivo_txt.read())

# Para dejar cursor en la sugunda linea se pede hacer con esta manera
# archivo_txt.seek(len(archivo_txt.readline()))
# print(archivo_txt.read())

# archivo_txt = open("/home/dtrl/GitHub/LessonsPython/src/main/resources/cuna.txt")
# print(archivo_txt)

# Para procearlo linea a linea, es posible hacerlo de la siguente forma:
# for linea in archivo_txt:
#     print(linea)

# Es posible obtener todas las lineas del archivo utilizando una sola llamada:
# lineas = archivo_txt.readlines()
# print(lineas)

# Es importante tener en cuenta que cuando se utilisa funciones como readlines(), se esta cargando en memoria el fichero
# completo. Siempre que una instruccion carge un fichero compoleto debe tener cuidado de utilizarla solo con ficheros
# pequenos, ya que de otro modo podria agotarse la memoria.

# Si quiremos eliminar los saltos de linea podemos usar la funcion rstrip(), que ademas sirve para eliminar los espacios
# en blanco de los extremos de un string.
# primeraLinea = lineas[0].rstrip()
# print(primeraLinea)

# print(archivo_txt.read())

# archivo_txt.close()

# ----------------------------------------- Creacion y escritura archivo -----------------------------------------------
# Si queremos abrir un fichero en modo escritura, hay que indicarlo como segundo parametro de la funcion open() pasando
# 'w' de write. Si la funcion no le pasamos un segundo parametro se utiliza el valor por defecto 'r' de read.
# arch_write = open("/home/dtrl/GitHub/LessonsPython/src/main/resources/nuevoFicheroW.txt", 'w')
# Aqui el fichero se va a crear aunque no exista antes para que podamos anadir contenido.

# Copiar en el nuevo fichero solo lineas pares del fichero anterior:
# for i, linea in enumerate(lineas):
#     if i % 2 == 0:
#         arch_write.write(str(i) + ' ' + linea)
#     else:
#         pass
# Al terminar de trabajar con un fichero, es recomendable cerrarlo ya que lo que se haya escrito no se guardara realmente
# hasta no cerrar el fichero.
# arch_write.close()
# Podemos comprobar el contenido del fichero nuevoFicheroW.txt
# arch_read = open("/home/dtrl/GitHub/LessonsPython/src/main/resources/nuevoFicheroW.txt", 'r')
# fileRead = arch_read.readlines()
# print(arch_read)


# archivo_txt = open("/home/dtrl/GitHub/LessonsPython/src/main/resources/archivoCreadoDesdePython.txt", "w")
# str = "Estupendo dia para estudiar Python. \nSiguente linea escrita en el archivo"
# archivo_txt.write(str)
# archivo_txt.close()

# ---------------------------- Agregacion de informacion a un archivo que ya existe ------------------------------------
# Abrir en modo escritura posicionandose al final del archvo.
    # En este caso se crea fichero, si no existe, pero en caso de que exista se posiciona al final, manteniendo el contenido
    # oreginal. Se usa 'a' como segundo parametro:
ficheroAppend = open("/home/dtrl/GitHub/LessonsPython/src/main/resources/nuevoFicheroW.txt", 'a')
ficheroAppend.write('\nEste es el final')
ficheroAppend.close()
lineas = open("/home/dtrl/GitHub/LessonsPython/src/main/resources/nuevoFicheroW.txt", 'r')
print(lineas.readlines())


# archivo_txt = open("/home/dtrl/GitHub/LessonsPython/src/main/resources/archivoCreadoDesdePython.txt", "a")
# Esli nado napisat tekst s novoi strochki nado v nachalo dobavit \n, a esli etoho ne zdelat to tekst dobavitsa priam
# posle posledneho smvola v archive
# str = "\nLa trecera linea escrita desde Python!!!"
# archivo_txt.write(str)
# archivo_txt.close()

# ---------------------------- Para poner modo alaves de lectura y escritura
# archivo_txt = open("archivoCreadoDesdePython.txt", "r+")


