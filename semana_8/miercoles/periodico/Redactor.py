import random 
from Articulos8 import Article

class redactor:
    def __init__(self,nombre,cedula):
        self.nombre = nombre
        self.cedula = cedula
    
    def escribir(self):
        print("Estoy escribiendo un art")
        articulo = Article (input:("Titulo: "),
        input:("Articulo: ")
        input:("Articulo: ")
        input:("Articulo: ")
        input:("Articulo: ")
        input:("Articulo: "))
        print("Termine")
        return articulo

class jefered(redactor):
    def __innit__(self,nombre,cedula,grupo):
        redactor.__init__(self,nombre,cedula)
        self.grupo = grupo
    
    def supervisar(self):
        print("Todo esta bien con los redactores")
    
    
    def decidir(self,articulo):
        if random.random()>0.5:
            print("El articulo",articulo,"fue aprobado")
        else:
            print("El articulo",articulo,"no fue aprobado")
