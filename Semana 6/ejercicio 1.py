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
    products = {"Q":{
        "name":"Quimico",
        "price" :1000
         }, 
         "F":{
            "name":"Farmaceutico",
         "price":2500
         }, 
         "B":{
            "name":"Biologico",
         "price":4000
         }}
    cliente_f=0
    cliente_b= 0
    cliente_q=0
    descuento_c=0
    descuento_r = 0
    rif_max = 0
    count = 0
    max_purchase = 0
    total_day = 0
    while True:
            rif = input("Por favor ingrese su RIF: ")
            tipo_estudio = input("Por favor ingrese su estudio: \n F - Farmaceutico \nQ - Quimico \nB - Biologico \n>> ")
            payment_type = input("Por favor ingrese su metodo de pago: \nC - De contado \nR - Credito \n>> ")

            descuento = 0
            tax = 0
            total_bruto = products.get(tipo_estudio).get("price")
            #descuento
            if payment_type == "C":
                descuento += total_bruto*0.03
            if total_bruto %2 == 0:
                descuento += total_bruto*0.02
            if is_prime(rif):
                descuento += total_bruto * 0.05
            #taxes
            if tipo_estudio != "F":
                tax = total_bruto*0.12
            #total
            total_pago = total_bruto+tax-descuento
           #final day
            if tipo_estudio == "F":
                cliente_f +=1
            if tipo_estudio == "Q":
                cliente_q +=1
            if tipo_estudio == "B":
                cliente_b +=1
            if payment_type == "C":
                descuento_c += descuento
            if payment_type == "R":
                descuento_r += descuento
            if total_pago > count:
                rif_max = rif
                max_purchase = total_pago
            
           
           
           
           
            #Factura
            print("_____________________")
            print("********RECEIPT******")
            print("_____________________")
            print("Rif: ",rif)
            print("Tipo de estudio: ",tipo_estudio)
            print("Metodo de pago: ",payment_type)
            print ("IVA: ", tax)
            print ("Descuento",descuento)
            print ("Total a pagar: ",total_pago)
            print("_____________________")

            if input ("Quiere salir? \nSI \nNO \n>>>") == "SI":
                break
    print ("__________________")
    print ("****CIERRE DIA*****")
    print ("Clientes F",cliente_f)
    print ("Clientes B",cliente_b)
    print ("Clientes Q",cliente_q)
    print ("Rif max compra",rif_max)
    print ("Compra mas alta",max_purchase)



            



main()