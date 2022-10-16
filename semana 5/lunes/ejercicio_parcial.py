def print_welcome ():
    print ("________________________")
    print ("Welcome <3")
    print ("_________________________")

def welcome_2 ():
    print ("What are you looking for today")


def get_user (dict):
    for key , values in dict.items():
        for key_interno , value_interno in values.items():
            print (f"{key_interno} - {value_interno}",end="\n")
        print ("")
        print ("________________________")
    return input ("please enter an option: \n Ultra Sonido \n Tomografia \n Radiografia \n -> ")

def get_client_data(study):
    client = {"name" : input("please write your name: ").lower,
    "id" : input("please write your id: "),
    "age" : input("please write your age: "),
    "gender" : input ("please write your gender M or F: ") ,
   "study" : study,
   }
    return client

def print_invoice(client):
    print ("___________________________")
    print("***RECEIPT****")
    print ("___________________________")
    print("ID " , client.get("id"))
    print ("Age ", client.get("age"))
    print ("gender ",client.get("gender"))
    print ("study ", client.get("study"))
    print ("Price" , client.get("price"))
    print ("___________________________")

def main():
    studys_dict_values = {"U":{
        "name":"Ultra sonido",
        "price" : 8900
         }, 
         "T":{
            "name":"Tomografia",
         "price":12640
         }, 
         "R":{
            "name":"Radriografia",
         "price":15600
         }}
    clients = []
    print_welcome()
    welcome_2()
    while True:
        option_menu = input("Please enter a option: \n1 Show the catalog and make a purchase \n2 See the total clients \n3 exit \n -> ")
        if option_menu.isnumeric():
            option_menu = int(option_menu)
            if option_menu == 1:
                option = get_user (studys_dict_values)
                client = get_client_data(option)
                print_invoice(client)
                clients.append[client]
            elif option_menu== 2:
                print (clients)
        else: 
            option_menu = input("Please enter a valid option")

main()