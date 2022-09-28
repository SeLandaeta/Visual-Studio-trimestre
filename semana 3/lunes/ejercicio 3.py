number = input("please enter  a number of floors for your trisngle -> ")
aux = 1

if number.isnumeric():
    number = int (number)
    number = number +1 
    for number in range (1, number, 2):
        if number * 2 - 1 == 1 :
            print (number * 2 -1)
        else: 
            print (number*2 -1, end=" ")
        



else:
    print ("error")





