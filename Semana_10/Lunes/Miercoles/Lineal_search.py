#ordenar siempre antes de buscar
from seleccion_sort import selection
def main():
    lista = [6,5,3,1,8,7,2,4]
    print ("______________________")
    lista = selection(lista)
    print ("______________________")

    number = int(input("Please enter a number: "))
    if binarysearch(number,lista)  :
        print(f"The number {number} is present")
    else: 
        print ("The number is not present")


def binarysearch(number,lista):
    start = 0
    final = len(lista) - 1
    middle = (start + final) // 2 #sumar siempre el low
    if len(lista) == 1:
        if lista[0] == number:
            return number 
        else: 
            return False

    if number > lista[middle]:
        return binarysearch(number,lista [middle : final])
    elif number < lista[middle]:
        return binarysearch(number,lista [start : middle])
    else: 
        return lista[middle]





main()