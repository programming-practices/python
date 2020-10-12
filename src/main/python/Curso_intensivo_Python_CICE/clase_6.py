
import math

class Circle:
    def __init__(self, radio):
        self.radio = radio
        self.area = 0
        self.perimetro = 0

    def calc_area(self):
        """esta funccion calcual el area usada el radio de la circle:"""
        self.area = math.pi * (self.radio ** 2)
        return round(self.area, 2)

    def calc_perimetro(self):
        self.perimetro = 2 * math.pi * self.radio
        return round(self.perimetro, 2)

    def escala(self, factor = 2):
        self.radio = factor * self.radio
        print(f"El nuevo radio es {self.radio}")
        print(f"El nuevo area es {self.calc_area()}")
        print(f"El nuevo parametro es {self.calc_perimetro()}")


class Contacto:
    def __init__(self, surname, name, telephone, email):
        """Antity of contact."""
        self.surname = surname
        self.name = name
        self.telephone = telephone
        self.email = email

    def getSurName(self):
        return self.surname

    def getName(self):
        return self.name

    def getTelephono(self):
        return self.telephone

    def getEmail(self):
        return self.email

    def setSurName(self, new_surname):
        self.surname = new_surname

    def setName(self, new_name):
        self.name = new_name

    def setTelephono(self, new_telephono):
        self.telephone = new_telephono

    def setEmail(self, new_email):
        self.email = new_email

    def descripcion(self):
        return "SurName: " + self.surname + " | Name: " + self.name + " | Telephono: " + str(self.telephone) + " | Email: " + self.email


class Agenda:
    def __init__(self):
        """Antity of agenda."""
        self.dictionaryContacts = {}

    def readContacts(self):
        """Read all contacts from the agenda"""
        # for con in self.dictionaryContacts.values():
        #     print(con.descripcion())

        for con in self.dictionaryContacts:
            print(f"{con}   {self.dictionaryContacts[con].descripcion()}")

    def updateAll(self, contacto, new_SurName, new_Name, new_Telephono, new_Email):
        if self.dictionaryContacts.__contains__(contacto.getSurName() + ' ' + contacto.getName()):
            temp = Contacto(new_SurName, new_Name, new_Telephono, new_Email)
            self.addContacto(temp)
            self.deleteContacto(contacto)
        else:
            print(f"{contacto.descripcion()} this contact not exist in the agend and therefore can not be updated.")

    def updateSurName(self, contacto, new_SurName):
        if self.dictionaryContacts.__contains__(contacto.getSurName() + ' ' + contacto.getName()):
            temp = Contacto(new_SurName, contacto.getName(), contacto.getTelephono(), contacto.getEmail())
            self.addContacto(temp)
            self.deleteContacto(contacto)
        else:
            print(f"{contacto.descripcion()} this contact not exist in the agend and therefore can not be updated.")

    def updateName(self, contacto, new_Name):
        if self.dictionaryContacts.__contains__(contacto.getSurName() + ' ' + contacto.getName()):
            temp = Contacto(contacto.getSurName(), new_Name, contacto.getTelephono(), contacto.getEmail())
            self.addContacto(temp)
            self.deleteContacto(contacto)
        else:
            print(f"{contacto.descripcion()} this contact not exist in the agend and therefore can not be updated.")

    def updateTelephono(self, contacto, new_Telephono):
        if self.dictionaryContacts.__contains__(contacto.getSurName() + ' ' + contacto.getName()):
            contacto.setTelephono(new_Telephono)
        else:
            print(f"{contacto.descripcion()} this contact not exist in the agend and therefore can not be updated.")

    def updateEmail(self, contacto, new_email):
        if self.dictionaryContacts.__contains__(contacto.getSurName() + ' ' + contacto.getName()):
            contacto.setEmail(new_email)
        else:
            print(f"{contacto.descripcion()} this contact not exist in the agend and therefore can not be updated.")

    def deleteContacto(self, contacto):
        """Remove the contact from agend."""
        if self.dictionaryContacts.__contains__(contacto.getSurName() + ' ' + contacto.getName()):
            self.dictionaryContacts.pop(contacto.getSurName() + ' ' + contacto.getName())
        else:
            print(f"{contacto.descripcion()} this contact not exist in the agend and therefore can not be delete!.")

    def addContacto(self, contacto):
        """Add the contact in agenda."""
        if self.dictionaryContacts.__contains__(contacto.getSurName() + ' ' + contacto.getName()):
            print(f"{contacto.descripcion()} this contact already exists in the agenda and therefore can not be added.")
        else:
            self.dictionaryContacts[contacto.getSurName() + ' ' + contacto.getName()] = contacto


agenda = Agenda()

# Creacion contactos
contactoAndres1 = Contacto("Garcia", "Andres", 44444444, 'email@email.com')
contactoAndres2 = Contacto("Garcia2", "Andres2", 4444444477, 'email55@email.com')
contactoAndres3 = Contacto("Garcia3", "Andres3", 444443333344477, 'email3355@email.com')
contactoAndres4 = Contacto("Garcia4", "Andres4", 444443333344444477, 'email335544@email.com')
# print(contactoAndres.descripcion())



# Agregar Contacto
agenda.addContacto(contactoAndres1)
agenda.addContacto(contactoAndres2)
agenda.addContacto(contactoAndres3)
# agenda.addContacto(contactoAndres3)

# Read contactos
agenda.readContacts()

# Borrar Contacto
agenda.deleteContacto(contactoAndres3)
# agenda.deleteContacto(contactoAndres4)
agenda.readContacts()

print("---------- Updarte ----------")
# Update Contacto
agenda.updateAll(contactoAndres2, "qqqqqqqq", "eeeeeeeeee", 111111111111, "eeeee@eeee.eee")
# agenda.updateSurName(contactoAndres3, "VVVVVVVVVV")
# agenda.updateSurName(contactoAndres2, "VVVVVVVVVV")
# agenda.updateName(contactoAndres2, "VVVVVVVVVV")
# agenda.updateTelephono(contactoAndres2, 00000000000000000000)
# agenda.updateEmail(contactoAndres2, "rrrr@email.com")
agenda.readContacts()


