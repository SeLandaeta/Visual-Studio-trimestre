#ejercicio farmacia
def welcome():
    print("________________")
    print ("***WELCOME***")
    print ("_______________")
def is_prime(rif):
    numero = int(rif[len(rif)-1])
    cont = 0 
    aux = numero - 1 
    while aux > 1:
        if numero % aux == 0:
            return False 
        aux -= 1 
    return True 

def main():
    farmacia = {"descripcion":{"Q":{"name":"Quimico","price":10},"F":{"name":"Farmaceuticos","price":25},"B":{"name":"Biologicos","price":45}}}
    clientesQ=0
    clientesF=0
    clientesB = 0
    clientesC = 0
    clientesR = 0
    recargo = 0
    totalfactu = 0
    while True:
        opcion = input("Por favor indique que desea hacer: \n1-Comprar \n2-Cerrar Dia \n>> ")
        if opcion == "1":
            descuento=0
            tax=0
            producto = input("Por favor ingrese el tipo de estudio que desea: \nQ-Quimico \nF-Farmaceuticos \nB-Biologicos \n>>").upper()
            rif = input("Por favor ingrese su RIF: ")
            metodo = input("Por favor ingrese su metodo de pago: \nC-Contado \nR-Credito \n >>")
            monto_neto = farmacia.get("descripcion").get(producto).get("price")
            if metodo == "R":
                recargo += monto_neto*0.10
                clientesR += 1 
            if monto_neto % 2 == 0:
                descuento += monto_neto*0.02
            if metodo == "C":
                descuento += monto_neto*0.03
                clientesC +=1
            if producto == "Q":
                tax += monto_neto*0.16
                clientesQ+=1

            if producto == "B":
                tax += monto_neto*0.16
                clientesB+=1
            if producto == "F":
                clientesF += 1
            if is_prime(rif):
                descuento += monto_neto*0.05
            montotot = monto_neto + tax  - descuento
            totalfactu += montotot


            print("_______________________________")
            print("***********RECIBO**************")
            print ("______________________________")
            print ("Rif:",rif)
            print("Producto: ",farmacia.get("descripcion").get(producto).get("name"))
            print("Metodo de pago: ",metodo)
            print ("Total brutp: ",monto_neto)
            print("Descuento: ",descuento)
            print("IVA: ",tax)
            print("Monto con descuento e IVA aplicados: ",montotot)
            print("_______________________________")
            
            


                
        else:
            break

    print("______________________________")
    print ("********Cierre de Dia*******")
    print ("_____________________________")
    print ("Compradores de Farmaceuticos: ",clientesF)
    print ("Compradores Quimicos: ",clientesQ)
    print ("Compradores Biologicos: ",clientesB)
    print ("Total facturado: ",totalfactu)
    print ("_____________________________")


main()
