from re import U


while (True):

    comprar = input ("Bienvenidos a FLighnit ¿Quiere comprar un par de zapatos? (s/S => si) (N/n => no) \n ")

    if comprar.upper() == "S": 
        zapatos = input ("""QUE ZAPATOS QUIERES? 
     Tacones => (T)
     Deportivos => (D)
     Sandalias => (S)
     : """)


        if zapatos.upper()== "T":
            print ("Gracias por comprar estos tacones")
            break
        elif zapatos.upper()=="D":
            print ("Gracias por comprar estos zapatos deportivoss")
            break
        else:
             print ("gracias por comprar estas sandalias")
        

    elif comprar.upper() == "N":
      print ("Que mal gusto de zapatos tienes")
     
      break 

    
    else: 
        print ("Error en el ingreso de datos, por favor ingreselo de nuevo")
