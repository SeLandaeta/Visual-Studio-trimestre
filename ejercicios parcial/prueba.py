#ejercicio 2 parcial 1 
def welcome ():
    print("******WELCOME TO LSU*******")

def pedir_cedula ():
    cedula = int(input("Please enter your ID: \n"))
    return cedula

def pedir_promedio():
    promedio = int(input("Please enter your grade points average betwen 20 and 0: \n "))
    return promedio


def main():
    welcome()
    dos = []
    uno=[]
    reprobado=[]
    dos_notas = []
    uno_notas = []
    reprobado_notas = []
    alumnos_total=[]
    while True:
        option = input("Please enter an option \nA-Apply for our program \nE-Exit \n")
        if option == "A":
            cedula = pedir_cedula()
            promedio = pedir_promedio()
            if  promedio >= 18:
                dos.append(cedula)
                dos_notas.append(promedio)
                alumnos_total.append(cedula)
                print("You have been selected for the second period")
            elif  promedio>= 12 :
                uno.append(cedula)
                uno_notas.append(promedio)
                alumnos_total.append(cedula)
                print ("You have been selected for the first period")
            elif promedio < 12 :
                reprobado.append(cedula)
                reprobado_notas.append(promedio)
                alumnos_total.append(cedula)
                print("You have been rejected ")
            
        
        elif option == "E":
            print ("___________________________________________________________________________")
            print ("******************************DAY SUMMARY**********************************")
            print ("___________________________________________________________________________")
            print ("There have been",len(alumnos_total),"students trying to get into the program")
            print ("There are",len(dos),"students in the second period")
            print ("There are",len(uno),"students in the first period")
            print ("There are",len(reprobado),"students rejected")
            print ("__________________________________________________________________________")
            suma=sum(uno_notas)
            if len(uno_notas)!=0:
                promedio_uno = suma/len(uno_notas)
            print("The points average per student in the first period is: \n",promedio_uno)
            suma2 = sum(dos_notas)
            if len(dos_notas)!=0:
                promido_dos = suma2/len(dos_notas)
            print("The points average per student in the second period is: \n",promido_dos)
            suma3 = sum(reprobado_notas)
            if len(reprobado_notas)!=0:
                promedio3= suma3/len(reprobado_notas)
            print("The points average per student in the first period is: \n",promedio3)
            promediotot= (promedio3 + promedio_uno + promido_dos )/3
            print("The total average betwen each period is:",promediotot)
            print ("____________________________________________________________________________")


            break


main()