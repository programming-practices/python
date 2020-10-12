
# Datos
ciudades_italianas = ['Roma', 'Milan', 'Napoles', 'Turin', 'Palermo', 'Genova', 'Bolonia', 'Florencia', 'Bari', 'Catania']
poblacion = [2718768, 1299633, 973132, 908263, 663173, 610887, 372256, 364710, 322511, 298957]

# Funciones
def crear_ranking(cuidades, pob):
    num = range(1, len(pob)+1)
    pares = zip(num, cuidades)
    d = dict(pares)
    d2 = {i+1 : [d[i+1], x] for i,x in enumerate(pob)}
    return d2
def get_pob(num, rank):
    """
        Dado un numero entero 'num' y un ranking de ciudades 'rank' , devuelve la ciudad que ocupa ese numero en el
        raking de ciudades.
    """
    if num in rank:
        return rank[num]
    else:
        return 0