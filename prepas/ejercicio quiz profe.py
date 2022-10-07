def main():
    numero = (input(f"Por favor escriba un numero primo: "))

    n = 0
    cont = 0 
    if numero.isnumeric():
        numero = int(numero)   
        while n <= numero:
            fermat = (2**2**n)+1
            if fermat == numero: 
                cont = cont + 1
            n = n+1
        if cont == 1: 
            print ("tu numero es un numero de fermat")
        else:
             print ("tu numero no es un numero de fermat")
    else:
        numero = input("Por favor introduzca un numero valido: ")
        n = 0
        cont = 0 
        if numero.isnumeric():
            numero = int(numero)   
            while n <= numero:
                fermat = (2**2**n)+1
                if fermat == numero: 
                    cont = cont + 1
                n = n+1
            if cont == 1: 
                print ("tu numero es un numero de fermat")
            else:
                print ("tu numero no es un numero de fermat")
main()


        