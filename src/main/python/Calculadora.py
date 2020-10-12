
# coding: utf-8

# In[ ]:


#MÓDULO DE EJEMPLO:

def suma(a,b,*numeros):
    resultado=a+b
    for i in numeros:
        resultado=resultado+i
    print(resultado)
    
def resta(a,b,*numeros):
    resultado=a-b
    for i in numeros:
        resultado=resultado-i
    print(resultado)
    
def multiplicacion(a,b,*numeros):
    resultado=a*b
    for i in numeros:
        resultado=resultado*i
    print(resultado)
    
def division(a,b):
    resultado=a/b
    print(resultado)

