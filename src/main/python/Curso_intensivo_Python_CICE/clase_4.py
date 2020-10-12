

diccionario = {"Alberto":9, "Chema":8, "David":10, "Andres":5, "Lucia":9, "Elena":6, "Sandra":4, "Julio":6, "Jorge":8, "Bea":7}
result = "{} ha sacado un {}"
for alumno in diccionario:
    print(result.format(alumno, diccionario.get(alumno)))





