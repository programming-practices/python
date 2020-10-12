
# coding: utf-8

# In[9]:


#MÓDULOS Y PAQUETES.

#Un módulo es una librería pequeña.
#Un paquete es un conjunto de módulos.

#Tres formas de importar un módulo .py:


# In[7]:


#Primera forma: Importa todo el módulo Calculadora pero hace falta referenciar el objeto.

import Calculadora

Calculadora.suma(1,2,3) #Llamamos a suma referenciando a Calculadora.


# In[4]:


#Segunda forma: Importa la función resta del módulo Calculadora.

from Calculadora import resta

resta(20,10,5)
suma(5,5) #Al no estar importado da error.


# In[6]:


#Tercera forma: Importa todo el módulo Calculadora. No hace falta referenciar.

from Calculadora import *

multiplicacion(8,8,8)
division(100,50)

