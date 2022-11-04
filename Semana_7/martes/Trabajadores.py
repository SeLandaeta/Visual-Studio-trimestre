from Articulos1 import articulo

class Persona:
    def __init__(self,nombre,cedula):
        self.nombre = nombre 
        self.cedula = cedula


class Redactor(Persona):
    def __init__(self,nombre,cedula,seccion):
        Persona.__init__(self,nombre,cedula)
        self.innit=seccion

    def escribir(self,titulo,resumen,cuerpo,imagenes,fechaCre,fechaPub,redactor):

        return articulo (titulo,resumen,cuerpo,imagenes,fechaCre,fechaPub,redactor,self.cedula )

    
class Jefe_redactor(Redactor):
    def __init__(self,nombre,cedula,seccion,group):
        Redactor.__init__(self,nombre,cedula,seccion)
        self.group = group
