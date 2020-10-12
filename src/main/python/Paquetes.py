
# Que son paquetes:
    # Directorios donde se almacenaran modulos relacionados entre si.
# Para que sirven paquetes:
    # Para organizar y reutilizar los modulos.
# Como se crea una paquete:
    # Tan sencillo como crear una carpeta con un archivo __init__.py

# Los paquetes son una manera de structurar y organizar los modulos. Se accede a los nombres de modulos con puntos.
# Por ejemplo, el nombre de modulo A.B designa un submodulo llamado B en un paquete llamado A.
# Los archivos __init__.py se necesitan para indicar a Python que se trata de un paquete que contiene otros paquetes.
# En el caso mas simple, __init__.py puede ser solamente un fichero vacio, pero tambien puede ejecutar codigo de
# inicializacion para paquete.
# Los usuarios del paquete pueden inportar modulos individuales del mismo, por ejemplo:
            # import MiCodigo.MisFuciones.funciones_orden