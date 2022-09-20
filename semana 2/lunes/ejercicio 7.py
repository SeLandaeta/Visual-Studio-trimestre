print ("Welcome to Bella Napoli")
option = input ("please enter an option: \n1- Vegetarian \n2- Non vegetarian\n- ->")
if option.isnumeric():
    option=int(option)
    if option == 1:  
        ingredient = input ("please enter an ingredient: \n1- Tofu \n2- Pimiento \n- ->")
        if ingredient == "1": 
            ingredient = "Tofu"
        else: 
            ingredient == "pimiento"
        print (f"You have ordered a vegetarian pizza with {ingredient}")
    elif option == 2: 
        ingredient = input ("please enter an ingredient: \n1- Peperoni\n2- Jam \n3- Salmon\n- ->")
        if ingredient == "1":
            ingredient = "Peperoni"
        elif ingredient == "2":
            ingredient = "Jam"
        else: 
            ingredient == "Salmon"
        print (f"You have ordered a non vegetarian pizza with {ingredient}")
    else:
        print("invalid number")
else: 
    print ("error")
    

