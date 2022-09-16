from tkinter import N


numEstudiantes= int (input("Ingrese el numero de estudiantes:"))

if numEstudiantes == 0:
     print ("nadie vino a mi clase")

if numEstudiantes > 0 and numEstudiantes <= 5: 
    print ("vinieron como mucho, 5 personas a mi clase")

if numEstudiantes %2: 
    print ("vinieron un numero par de estudiantes")

if not numEstudiantes %2: 
    print ("vinieron un numero impar de estudiantes")

if numEstudiantes >= 14 and numEstudiantes <= 15: 
    print ("vinieron casi todos los estudiantes")
