def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def potencia(base,exponente):
    #base = int(input("Por favor ingrese la base de su operacion"))
    #exponente = int(input("Por favor ingrese el exponente de su operacion"))
    if exponente == 1:
        return base 
    return base*potencia(base,exponente - 1)

def main():
    #base = int(input("por favor inngrese una base: "))
    
    #exponente = int(input("por favor inngrese una exponente: "))
    print(potencia(int(input("por favor inngrese una base: ")),int(input("por favor inngrese una exponente: "))))
main()