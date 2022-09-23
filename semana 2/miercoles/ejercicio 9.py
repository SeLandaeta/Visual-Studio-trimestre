number = int (input ("Please enter a number: "))
aux = number - 1 
acum = 0


while aux > 2: 
     if number % aux == 0:
          acum += aux
     aux -= 1 

if number < acum : 
    print (f"The number {number} is abundant")
