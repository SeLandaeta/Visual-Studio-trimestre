from ast import Try
from multiprocessing.connection import deliver_challenge


def welcome():
    print ("^^^BIENVENIDO A PAPAS PIZZA^^^")

def mostrarmenu(menu):
    print ("Por favor elija una pizza \n")
    for pizza in menu: 
        igredientlista=list(ingrediente for ingrediente in pizza["ingredientes"])
        ingredientes = ", ".join (igredientlista)
        print(f"""nombre:{pizza["pizza"]}
        ingredientes:{ingredientes}
        Tipo de precio segun coccion:
                a la parrilla:{pizza["precio"]["a la parrilla"]} 
                a la leña: {pizza["precio"]["a la leña"]}""")

def realizar_compra(menu,tipospizzaspedidas,CantidadTamanoPedidas):

    while True:
            pizza=input("Por favor ingrese el nombre de la pizza que desea:\n")
            tiponum = int(input("Por favor ingrese que tipo de coccion desea \n1-> a la parrilla \n2-> a la leña\n->>"))
            if tiponum == 1:
                tipo = "a la parrilla"
                print (tipo)
            elif tiponum == 2:
                tipo = "a la leña"
            costo = 0
            for pizzaDic in menu:
                if pizzaDic["pizza"] == pizza:
                    costo = int(pizzaDic["precio"][tipo][:-1])
            tamanospermitidos = [8,10,12]
            tamano = int("Por favor elija un tamano para su pizza: \n-> 8  \n-> 10 \n3 -> 12 \n->")
            if tamano == 8:
                costo += 0
            elif tamano == 10:
                costo +=5
            elif tamano == 12:
                costo += 10
            cantidad = int(input("Por favor ingrese la cantidad de pizzas que desea \n"))
            break
            costo = cantidad*costo
            tipospizzaspedidas[pizza]+=1
            CantidadTamanoPedidas[tamano]+=1

            return pizza,tipo,costo,tamano,cantidad 

def formato_pago():
    while True:
        metodos_validos =["Zelle","Debito","Efectivo"]
        try:
            formato=input("Por favor ingrese su metodo de pago: ").capitalize().strip()

            if formato not in (metodos_validos):
                raise Exception
            return formato
        except:
            print ("por favor favor ingrese un metodo valido")

def Primos(num):
    for i in range(2,num):
        if num %i == 0:
            return False 
        else:
            return True 

def Cedula():
    while True:
        try:
            descuento = 1
            cedula = (input("Por favor ingrese su cedula: \n"))
            if Primos(int(cedula[-1])):
                 descuento = 0.95
            return cedula, descuento
        except:
            print("Ingrese un valor valido")

def Nombre():
    while True:
        try:
            nombre = input("Por favor ingrese su nombre: \n")

            if not (nombre.isalpha()):
                raise Exception 
            return nombre 
        except: 
            print ("Ha ocurrido un error")

def pedir_datos():
    cedula,descuento = Cedula()
    nombre = Nombre()
    pagoformato = formato_pago()
    return nombre,pagoformato,cedula,descuento

def Comprar_pizzas(menu,delivery,idPedidos,pedidos,pedidosMunicipios,lista_pizza,tiopospizzaspedidas,CantidadTamanoPedidas):
    nombre,cedula,descuento,pagoformato = pedir_datos()
    while True:
        mostrarmenu(menu)
        pizza,tipo,costo,cantidad,tamano = realizar_compra(menu,tiopospizzaspedidas,CantidadTamanoPedidas)
        if lista_pizza == None:
            lista_pizza[pizza]={"precio":{costo},"tamano":{tamano},"tipo":{tipo},"cantidad":{cantidad}}
        pedidos[idPedidos] ={"Nombre":nombre,
        "Cedula":cedula, 
        "Formatopago":pagoformato,
        "Cantidadpizzas":cantidad,
        "Tamano":tamano,
        "Tipo":tipo,
        "Costo":costo,
        "Deliveryextra":0,
        "Descuento":descuento
        }

        try:
            opcion=int(input("Indique que desea hacer \n1 Seguir comprando \n2 Finalizar compra"))
            if opcion == 2:
                return pedidosMunicipios,pedidos,tiopospizzaspedidas,CantidadTamanoPedidas
            elif opcion == 1:
                idPedidos +=1
            else:
                raise Exception
        except:
            print ("Por favor ingrese un valor valido")

def CerrarCompra(delivery,pedidos,pedidosMunicipios,listapizzas):
    while True:
        for pedido in pedidos:
            print (pedido)
        try:
                deliveryopickup=int(input("Por favor ingrese como desea recibir su pizza: \n1-> Delivery \n2-> Pickup \n3-> "))
                if deliveryopickup == 1:
                    municipio=input("Por favor ingrese en que municipio se encuentra:  ").capitalize().strip()
                    if municipio not in delivery.keys():
                        raise Exception
                    else: 
                        pedido ["Deliveryextra"] += delivery[municipio]
                        pedidosMunicipios[municipio] += 1
                        break
                elif deliveryopickup == 2:
                    pass
        except:
            print("error")
        print(f"""Nombre: {pedido["Nombre"]}
        Cedula:{pedido["Cedula"]} 
        Formato de pago:{pedido["Formatopago"]}""")

        for nombre,datos in listapizzas.items():
            print(f""""Tipo de pizza: {nombre}
             Precio: {datos["Precio"]}
             Tamano: {datos["Tamano"]}
             Cantidad: {datos["Cantidad"]}""")

        Costo = pedido["Costo"]
        print(f"precio sin delivery ={Costo}")

        if pedido["Deliveryextra"]!= 0:
            Costo+=pedido["Deliveryextra"]
            print (f"precio con delivery: {Costo}")

        if pedido["Descuento"] != 0:
            Costo*=pedido["Descuento"]
        print (f"precio con descuento: {Costo}")
        
        break 


            

def main():

    delivery = {
        "Chacao":2,
        "Sucre":3,
        "Baruta":4,
        "El Hatillo":4,
        "Carrizal":4
    }

    lista_pizza = {}
    pedidos = {}
    tipospizzaspedidas= {"Margarita":0,"4 Estaciones":0,"Peperoni":0,"Prosciutto Funghi":0,"Española":0}
    CantidadTamanoPedidas= {8: 0,
    10: 0,
    12: 0}

    pedidosMunicipios = {
    "Chacao":0,
    "Sucre":0,
    "Baruta":0,
    "El Hatillo":0,
    "Carrizal":0}

    idPedidos = 0
    menu = [

   {

      "pizza":"Margarita",

      "ingredientes":[

         "salsa napolitana",

         "queso mozzarella"

      ],

      "precio":{

         "a la parrilla":"6$",

         "a la leña":"8$"

      }

   },

   {

      "pizza":"Pepperoni",

      "ingredientes":[

         "salsa napolitana",

         "queso mozzarella",

         "pepperoni"

      ],

      "tipo":"a la parrilla",

      "precio":{

         "a la parrilla":"8$",

         "a la leña":"10$"

      }

   },

   {

      "pizza":"4 Estaciones",

      "ingredientes":[

         "salsa napolitana",

         "queso mozzarella",

         "jamón",

         "maíz",

         "champiñones",

         "pimentones"

      ],

      "tipo":"a la parrilla",

      "precio":{

         "a la parrilla":"11$",

         "a la leña":"12$"

      }

   },

   {

      "pizza":"Prosciutto Funghi",

      "ingredientes":[

         "salsa napolitana",

         "queso mozzarella",

         "jamón",

         "champiñones",

         "aceite de oliva"

      ],

      "tipo":"a la parrilla",

      "precio":{

         "a la parrilla":"10$",

         "a la leña":"13$"

      }

   },

   {

      "pizza":"Española",

      "ingredientes":[

         "salsa napolitana",

         "queso mozzarella",

         "jamón serrano",

         "salchichón picante"

      ],

      "tipo":"a la parrilla",

      "precio":{

         "a la parrilla":"12$",

         "a la leña":"14$"

      }

   }

]
    welcome()
    while True:
            
        try:
            option = int(input("Por favor indique que quiere hacer hoy: \n1-Ver Menu \n2-Hacer Compra \n3-Cerrar compra \n4-Salir"))
            if option == 1:
                mostrarmenu(menu)
            elif option == 2:
                pedidos,pedidosMunicipios,tipospizzaspedidas,CantidadTamanoPedidas = Comprar_pizzas(menu,delivery,pedidos,idPedidos,lista_pizza,tipospizzaspedidas,CantidadTamanoPedidas,pedidosMunicipios)
            elif option == 3:
                    CerrarCompra(delivery,pedidos,pedidosMunicipios,lista_pizza)
            elif option == 4:
                break 
            else:
                raise Exception
        except:
            print("Por favor ingrese un numero valido")
            


main()