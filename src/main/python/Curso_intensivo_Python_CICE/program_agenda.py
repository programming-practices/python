#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:40:21 2018

@author: formador
"""

from Agenda import *

a = Agenda()



while True:
    print("Selecciona una opcion:")
    print("0 Listar agenda:")
    print("1 Añadir contacto:")
    print("2 Buscar contacto:")
    print("3 Borrar contacto:")
    print("4 Editar contacto:")
    print("5 Salir:")
    
    op = input(' ')
    
    if op.isnumeric():
        if int(op) in range(0,6):
            if int(op) == 0:
                a.list_agenda()
            elif int(op) == 1:
                c = Contacto()
                a.new_contact(c)
            elif int(op) == 2:
                term = input('pon tu termino de búsqueda: ')
                a.search(term)
            elif int(op) == 3:
                term = input('pon tu termino de búsqueda: ')
                a.del_contact(term)
            elif int(op) == 4:
                term = input('pon tu termino de búsqueda: ')
                a.update_contact(term)
            elif int(op) == 5:
                break
            else:
                print('not found')
        else:
            print('not found')