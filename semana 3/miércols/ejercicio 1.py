#key va siempre entre corchetes {key:(cualquier valor o palabra)}
elementos = {"hierro":1 , "Cobre":2}
elementos["litio"]=3 
print (elementos["litio"])
#si intentas imprimir un valor que no esta dara error
#si usamos .get no dara un error sino que imprimira "non", tambien puedes pasarle un valor deseado (x:valor por si no lo encuentra o palabra)
print(elementos.get("oxigeno","ME AHOGO"))
# for key , value in lista de keys .format()
#print (elementos.get(x)is none) -> esto sucede porque no le agrego otro valor 
#list1 is list2 no daria lo mismo ya que no estan igualadas, es decir no apuntan a la misma linea de memoria,
list1 = []
list2 =[]
list3 = list1 
if list1 == list2:
    print (True)
if list1 is list2:
    print (True)
if list1 is list3:
    print (True)