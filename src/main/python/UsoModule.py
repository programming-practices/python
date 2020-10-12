# Mozno tak import delat, no pri takom importe yxydwaetsa chitaimost
# import math, OS, random
# import math
# tak mozno skorochevat imia modula, tobto psevdonimu
# import random as r
# import mozno oborachevat v try except dlya pereverki na vsikii slychai esli modul ne sywchestvuet
# try:
#     import nomodule
# except ImportError:
#     print("Modyla nomodule ne suwestvuet")

# import sozdanoho modual
# import Modul

# Mozno importirovat modul tak
# from Module import resta, sumar  # esli importiruetsa mnoho funcii to nado pisat tak vso v duwkax from Module import (resta,suma, ...)
# no pri takim importe importiryetsa tolko ykazanui method ukazanaia function, i obratitsa k etomy methodu mozna s pomowchy
# tolko eho imeni resta, ne nado pisat imia modula v nachale Module.resta

# Takim sposobom mozno importirovat ves modul
# from Modulos.Module import *
# from src.main.python.Modulos.Module import *

# mozno propisevat  v imenax methodov sinonimu
# from Module import resta as re, sumar as su


# print(math.sqrt(3))
# print(r.random())

# Modul.sumar(3,3)

# resta(4, 5)
# sumar(3,4)

# re(4,5)
# su(3,4)

# multiplicar(3,4)


# miVehiculo = Vehiculo("Mazda", "MR5")
# print(miVehiculo.estado())

#-----------------------------------------------------------------------------------------------------------------------
import Modulos.CargarDatos as cd

# Usando el nombre del modulo CargarDatos a su alias cd poder acceder a las funciones definidas en el usando el operador punto:
it = cd.ciudades_italianas
p = cd.poblacion

r = cd.crear_ranking(it, p)
ciudad = cd.get_pob(1, r)
print(ciudad)

# Dependiendo de como hayamos importado el modulo, asi tendremos que utilizarlo:
    # Importamos solo la funcion crear_ranking :
    # Cuando se hace importe con esta manera, no hace falta llamar estas funciones con nombre de modulo, por
    # ejemplo CargarDatos.crear_ranking no hace falta hacer asi se puede hacer solo llamando la funcion crear_ranking
        # from CargarDatos import crear_ranking
        # from CargarDatos import crear_ranking, get_pob, poblacion, ....
        # ...
        # a = crear_ranking(c, p)
        # a
    # Importar todo el  modulo:
    # Cuando se hace este importe hay que siempre llamar al las funciones co esta manera CargarDatos.crear_ranking()
        # import CargarDatos
        # ...
        # a = CargarDatos.crear_ranking([2, 3, 4])
        # a
    # Se accede con alias a la funcion crear_ranking
    # Cuando se hace este importe hay que siempre llamar al las funciones co esta manera cd.crear_ranking()
        # import CargarDatos as cd
        # ...
        # a = cd.crear_ranking(c, p)
        # a