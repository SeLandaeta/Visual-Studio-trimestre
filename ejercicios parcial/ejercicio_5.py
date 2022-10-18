#ejercicio auto escuela
def welcome():
    print("____________________________")
    print("********BIENVENIDO*********")
    print("____________________________")
def pedir_cedula():
    cedula=input("Por favor ingrese su cedula:\n>>")
    return cedula
def pedir_nombre():
    name=input("Por favor ingrese su nombre: \n>>>")
    return name 
def pedir_practica():
    pract = input("Por favor ingrese que tipo de auto desea: \nA-Auto sincronico \nB-Auto automatico \n>>")
    return pract
def pedir_horas():
    horas =int(input("Por favor ingrese el numero de horas que desea practicar: \n>>"))
    return horas 
def main():
    drivers = {"A":{"tipo":"Vehiculo sincronico","pph":2500},"B":{"tipo":"Vehiculo automatico","pph":3500}}
    totalclientes = 0
    totalclientesA=0
    totalfacturadoA=0
    personasA = 0
    totalclientesB=0
    totalfacturadoB=0
    personasB = 0
    totaldescuentos = 0
    totaldescuentos=0
    welcome()
    while True:
        
        opcion = input("Por favor ingrese que desea realizar: \nR-Reservar un turno de practica \nC-Cerrar el dia \n>>")
        if opcion == "R":
            for key,values in drivers.items():
                for keys,value in values.items():
                    print (value)          
            cedula = pedir_cedula()
            nombre = pedir_nombre()
            practica = pedir_practica()
            horas=pedir_horas()
            descuento = 0
            pricehour = 0
            price = drivers.get(practica).get("pph")
            pricenet = 0
            pricenet=price-descuento
            pricehour = pricenet*horas
            if practica == "A":
                totalclientesA +=1
                totalfacturadoA += horas*pricenet-descuento
                totalclientes +=1
                personasA += 1
            if practica == "B":
                totalclientesB += 1
                totalfacturadoB += horas*pricenet
                totalclientes += 1
                personasB+=1
            if horas >= 3:
                descuento += price*0.15
                totaldescuentos += 1
            pricenet=price-descuento
            pricehour = pricenet*horas
            print ("_______________________")
            print ("*********RECIBO********")
            print ("_______________________")
            print ("CEDULA: ", cedula)
            print ("NOMBRE: ",nombre)
            print ("TIPO DE VEHICULO: ",drivers.get(practica).get("tipo"))
            print ("TOTAL A PAGAR: ",pricehour)
            print ("DESCUENTO POR HORA: ",descuento)
            print ("________________________")
            
        else:
            break
    print("_________________________")
    print("******CIERRE DE DIA******")
    print("_________________________")
    print("CANTIDAD TOTAL DE CLIENTES:",totalclientes)
    print("FACTURADO A: ",totalfacturadoA)
    print("FACTURADO B: ",totalfacturadoB)
    print("PERSONAS DESCUENTO: ",totaldescuentos)
    print("PERSONAS A: ",personasA)
    print("PERSONAS B: ",personasB)



            


        


main()