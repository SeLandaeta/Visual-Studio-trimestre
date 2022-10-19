#numeros ambiciosos
def hallardivisores(numero,divisoresnumero):
    aux = 0
    while aux < numero:
        aux+=1
        if numero%aux == 0:
            divisoresnumero.append(aux)
    divisoresnumero.pop(-1)
    return divisoresnumero

def hallardivisores_remix(sumadivisoresambiciosos,divisoresaux):
    aux = 0
    while aux < sumadivisoresambiciosos:
        aux += 1
        if sumadivisoresambiciosos%aux == 0:
            divisoresaux.append(aux)
    divisoresaux.pop(-1)
    return divisoresaux






def main():
    divisoresnumero=[]
    divisores_auxiliar=[]
    while True:
        numero = int(input("Por favor ingrese un numero natural: \n>>"))
        if numero <=0:
            print("Este numero no es un numero ambicioso")
        else:
            divisoresnumero = hallardivisores(numero,divisoresnumero)
            sumadivambiciosos = sum(divisoresnumero)
            divisores_auxiliar = hallardivisores(sumadivambiciosos,divisores_auxiliar)
            suma_aux = sum(divisores_auxiliar)
            if sumadivambiciosos == suma_aux:
                print(f"{numero} es un numero ambicioso")
            else:
                print(f"{numero} no es un numero ambicioso")
            opcion = input("Por favor ingrese el siguiente paso: \nC-Continuar \nS-Salir")
            if opcion == "C":
                continue 
            else:
                break
    print ("*************HASTA LUEGO**********************")

main()