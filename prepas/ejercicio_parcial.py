def bienvenida():
    print ("***Welcome***")

def ordenar_estudio(dict):
    estudios_disponibles = {"Ultrasonido":0,"Tomografia":1,"Radiografia":2}
    while True:
        try:
            estudio = input("Por favor ingrese el nombre del estudio que se quiere realizar: ").strip().capitalize()
            if estudio not in list (estudio["tipo"] for estudio in dict ):
                        raise Exception
            else:
                print (estudio)
            
            costo = 0
            

            for estudioselec in dict:
                if estudioselec["tipo"] == estudio:
                    costo = int(estudioselec["precio"][:-1])
            return estudio,costo

        except:
            print ("Algo salio mal en el proceso")

def hacer_pago():

 








def main (): 
    

    lista_estudios={}
    pedidos = {}
    tipos_estudios_ordenados = {"Ultra Sonido":0,"Tomografia":0,"Radiografia":0}
    estudios_dict_values = [


{

    "tipo":"Ultra Sonido",


    "precio":890
},

{

    "tipo":"Tomografia",

    "precio":1400
},

{
    "tipo":"Radiografia",

    "precio":1500
        }
    
]

    

    while True:
        try:
            option = input("Por favor ingrese una opcion: \n1 Agendar un estudio \n2 Revisar las ventas del dia \n3 Salir \n")
        except:
            hacer_pago()

main()