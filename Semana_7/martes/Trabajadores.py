class Redactor:
    def __innit__(self,nombre,cedula,seccion):
        self.innit=seccion
        self.innit=cedula
        self.nombre=nombre
class Jefe_redactor:
    def __innit__(self,nombre,cedula,seccion,group):
        Redactor.__innit__(self,nombre,cedula,seccion)
        self.group = group 

       
