num =  ( input("Escriba un numero entero: "))

if num.isnumeric(): 
    num = int (num)
    if num %2 == 0:
        print (f"El numero {num} es par")
    else: 
        print (f"El numero {num} es impar")

else: 
    print ("Error fatal")
 
