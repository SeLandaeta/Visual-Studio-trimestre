def print_welcome ():
    print ("Welcome <3")

def get_user (dict):
    for key , values in dict.items():
        for key_interno , value_interno in values.items():
            print (f"{key} - {value_interno}",end="")
        print ("")
    return input ("please enter an option:")

def get_client_data(study):
    client = {"name" : input("please write your name: ").lower,
    "id" : input("please write your id: "),
    "age" : input("please write your age: "),
    "gender" : input ("please write your gender M or F: ") ,
   "study" : study
    }
    return client

def print_invoice(client):
    print("***RECEIPT****")
    print("ID " , client.get("id"))
    print ("Age ", client.get("age"))
    print ("gender ",client.get("gender"))
    print ("study ", client.get("study"))
    print ("******************")





def main():
    studys_dict_values = {"U":{
        "name":"tomografia",
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
    print_welcome
    while True:
        option = get_user(studys_dict_values)
        client =get_client_data (option)
        print_invoice (client)       
        clients.append (client)

       

main()