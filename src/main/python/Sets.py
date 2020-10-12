
# Los conjunto o sets son colecciones no ordenadas de elmentos no repetidos. Los conjuntos pueden crearse de dos formas diferentes
    # Mediante una lista de elementos entre llaves { }
    # Mediante la funcion set()
s1 = set([3, 3, 3, 1, 1, 1, 2])
s2 = {3, 5, 6, 7, 7, 1, 1, 1, 2}

# Los conjuntos en Python admiten las operaciones matematicas habituales sobre conjuntos, como son la union, interseccion
# diferencia, etc.
    # Diferencia: s2 - s1
s3 = s2.difference(s1)
print(s1)
print(s2)
print(s3)
# La llamada help(set) o (s1. por ejemplo, en el editor) devuelve una lista de los methodos que se pueden aplicar a conjuntos.
# Esta estructura de datos resulta muy util cuando necesitamos eliminar elementos repetidos de una lista.
# lista inicial con elementos repetidos
lista = [3, 5, 6, 7, 7, 1, 1, 1, 2]
# Creamos un conjunto a partir de la lista
sin_repes = set(lista)
# Creamos una lista a partir del conjunto anterior
lista = list(sin_repes)
print(lista)