from Semana_7.lunes_py.Name import vehicle


class Vehiculo:
    def __innit__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas
    def decirvehiculo(self):
        print(f"Su vehiculo es de color {self.color} y tiene {self.ruedas} ruedas")

class Coche(Vehiculo):
    def __innit__(self, color, ruedas,velocidad,cilindrada):
        Vehiculo.__init__(self,color,ruedas)
        self.velocidad = velocidad 
        self.cilindrada = cilindrada
    def decirvehiculo(self):
        print(f"Su vehiculo es de color {self.color} , tiene {self.ruedas} ruedas, su velocidad maxima es de {self.velocidad}km/h y tiene una cilindrada de {self.cilindrada}")

class Camioneta(Coche):
    def __innit__(self, color, ruedas,velocidad,cilindrada,carga):
        Coche.__innit__(self, color, ruedas,velocidad,cilindrada)
        self.carga = carga 
    def decirvehiculo(self):
        print(f"Su vehiculo es de color {self.color} , tiene {self.ruedas} ruedas, su velocidad maxima es de {self.velocidad}km/h , tiene una cilindrada de {self.cilindrada} y su carga maxima es de {self.carga} ")

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        Vehiculo.__innit__(self,color,ruedas)
        self.tipo = tipo
    def decirvehiculo(self):
        print(f"Su vehiculo es de color {self.color} y tiene {self.ruedas} ruedas y del tipo {self.tipo}")

class Motocicleta(Bicicleta):
    def __innit__(self, color, ruedas,tipo, velocidad,cilindrada):
        Bicicleta.__innit__(self,color,ruedas,tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def decirvehiculo(self):
        print(f"Su vehiculo es de color {self.color} , tiene {self.ruedas} ruedas, su tipo es de {self.tipo}, su velocidad maxima es de {self.velocidad}km/h y tiene una cilindrada de {self.cilindrada}")
       