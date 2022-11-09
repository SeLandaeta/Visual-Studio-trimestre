def buscar(letra,lista,ind):
    if lista[ind] == letra:
        return letra
    elif len(lista)-1 == ind:
            if lista [ind] == letra:
                return letra 
            else:
                return None 
    return buscar(lista,letra,ind+1)







def main():

    lista = ["a","d","k","l","k","m","o"]
    letra  = input("Por favor ingrese una letra para buscar: ")
    print(buscar(letra,lista,0))
main()