# -*- coding: utf-8 -*-
"""

AGENDA:

"""

class Contacto:
    def __init__(self):
        self.name = input('Mete nombre: ')
        self.surname = input('dime apellido: ')
        self.telephone = input('cual es tu telefono???: ')
        self.email = input('pon tu email: ')
    
    def new_contact(self,name, surname, telephone, email ):
        self.name = name
        self.surname = surname
        self.telephone = telephone
        self.email = email
    
    def read_contact(self):
        print(f"{self.name} {self.surname}: \nTelefono: {self.telephone}\nemail: {self.email}")
    
    def update_name(self,name):
        self.name = name
    
    def update_surname(self,surname):
        self.surname = surname
            
    def update_tel(self,telephone):
        self.telephone = telephone
         
    def update_email(self,email):
        self.email = email  
    
    def del_data(self):
        self.name = ''
        self.surname = ''
        self.email = ''
        self.telephone = ''
        
class Agenda:
    def __init__(self):
        self.agendic = {}
    
    def search(self, term):
        shortlist = []
        for key in self.agendic:
            if term in key:
                shortlist.append(key)
        print(shortlist)
        i = 0
        while i < len(shortlist):
            print(i, shortlist[i])
            i += 1
        res = input('Cual es el contacto que querias? (dame el numero): ')
        print(res)
        if res.isnumeric():
            if int(res) < len(shortlist):
                key = shortlist[int(res)]
                print(key)
                print(self.agendic.get(key).read_contact())
            else:
                print('el numero introducido es demasiado alto')
        else:
            print('tenias que meter un numero, animal!')
        return key
        
    def new_contact(self, contact):
        #creo clave para el diccionario:
        key = contact.name+'_'+contact.surname
        #anado el contacto (objeto) al diccionario:
        self.agendic[key] =  contact
    
    def del_contact(self,term):
        key = self.search(term)
        #elimina un contacto de la agenda:
        if key in self.agendic:
            confirm = input(f'Seguro que quieres eliminar {key} de la agenda? (s/n): ')
            if confirm == 's':
                del self.agendic[key]
                print(f'Se ha borrado {key} de la agenda :)')
            elif confirm == 'n':
                print('pues me alegra de que te arrepientas')
            else: 
                self.del_contact(key)
        else:
            print(f'no hemos encontrado {key}')
    
    def list_agenda(self):
        for key in self.agendic:
            contact = self.agendic.get(key)
            print(key, contact.read_contact())
    
    def update_contact(self, term):
        key = self.search(term)
        field = input('que campo quieres editar? (telefono, email): ')
        contact = self.agendic.get(key)
        if field == 'telefono':
            new_tel = input(f'cual es el nuevo numero que tiene {key}?: ')
            contact.update_tel(new_tel)
        elif field == 'email':
            new_mail = input(f'cual es el nuevo email que tiene {key}?: ')
            contact.update_email(new_mail)
        print("contacto editado")

        
    
    
            
    
    
        
        
    
    
    
    
    
