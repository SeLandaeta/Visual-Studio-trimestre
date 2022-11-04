class anuncomer:
    def __init__ (self,seccion,imagen):
        self.imagen = imagen
        self.seccion = seccion

class anunclas:
    def __init__(self,dias,fechapubli,precio,tipo):
        self.precio = precio 
        self.fechapubli = fechapubli
        self.dias = dias
        self.tipo = tipo



class anunciovehi(anunclas):
    def __init__(self,dias,fechapubli,precio,marca,modelo,ano):
        anunclas.__init__(self,dias,fechapubli,precio,"vehiculo")
        self.marca = marca
        self.modelo = modelo
        self.ano = ano 

class anunvivi(anunclas):
    def __init__(self,dias,fechapubli,precio,m2,cuartos,puestos,politicas):
        anunclas.__init__(self,dias,fechapubli,precio,"vivienda")
        self.m2 = m2
        self.cuartos = cuartos 
        self.puestos = puestos 
        self.aceptapoliticas = politicas