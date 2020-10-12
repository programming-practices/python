
# Python es uno de los muchos lenguajes que permmiten programacion orientada a objetos (OOP, por su siglas en Ingles)
# Las classes en programacion intentan modelar datos de la forma en que se indealizan objetos de la vida real
# Un objeto de un clase tendra unos datos y una funccionalidad:
    # Datos:
        # Un determinado objeto tiene un conjunto de caracteristicas (denominadas atributos o propiedades), cada una de
        # las cueales tiene un valor. Estas caracteristicas indican cual es su estado actual
    # Las clases pueden tener una cantidad arbitraria de atributos de cualquier tipo.
    # Funcionalidad:
        # Los objetos responden a un conjunto de acciones(funciones o methodos) que pueden realisar.
# Notas acerca de la OOP en Python
    # Como en el caso de las funciones, si la primera linea del cuerpo de una clase se trata de una cadena de texto, esta
    # sera la cadena de documentacion de la clase docstring.
    # normalmente los miembros de las clases son "publicos". No existe en el estandart de Python el concepto de miembros
    # "privados", que no pueden accederse excepto desde dentro de un objeto. Sin embargo, hay una convencion que se sige
    # en la mayoria del codigo Python (ver PEP 08)
        # Un nombre prefijado con un guion bajo(_) deberia tratarse como debil de uso interno. Al importar un  modulo con
        # from m import *, ningun nombre que comience con _ se importara.
        # Un nombre prefijado con un guion double bajo (__) es un miembro privado y convierte el atributo mediante el
        # procedimento de name mangling a _clase__atributo. Se hace para evitar accidentes cuando se herede de una clase
        # con atributos privados.