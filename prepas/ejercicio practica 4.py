materias = ["Matematica","Biologia","Historia","Lenguaje","Deporte"]
notas = []
for materia in materias: 
    nota = (input("Que nota has sacado en " + materia + "? "))
    notas.append(nota)
for i in range(len(notas)):
    print ("Usted ha sacado " + notas[i] + " en " + materias [i]  )
