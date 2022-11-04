class Persona:
    def __init__ (self,nombre,apellido,edad,cedula):#primer metodo a llamar
        self.nombre = nombre 
        self.apellido = apellido
        self.edad = edad 
        self.cedula = cedula
    def mostrar(self):
        print (f"Mi nombre es {self.nombre}{self.apellido}, tengo {self.edad} anos, y mi cedula es {self.cedula}")

    