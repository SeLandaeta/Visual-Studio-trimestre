#sebastian landaeta 29.802.976


medications = {
        "prescription": {
            "antibiotics": {
                "skin": [
                    {
                        "id": 1,
                        "name": "Clindamicine",
                        "price": 300
                    },
                    {
                        "id": 2,
                        "name": "Cefadroxil",
                        "price": 350
                    },
                    {
                        "id": 3,
                        "name": "Amoxicillin",
                        "price": 320
                    }
                ],
                "respiratory-system":[
                    {
                        "id": 4,
                        "name": "Citromicine",
                        "price": 380
                    },
                    {
                        "id": 5,
                        "name": "Levofloxacine",
                        "price": 125
                    },
                    {
                        "id": 6,
                        "name": "Azitromicine",
                        "price": 740
                    }
                ]
            },
            "analgesic": {
                "anti-inflammatories": [
                    {
                        "id": 7,
                        "name": "HYDROCODONE-IBUPROFEN",
                        "price": 150
                    },
                    {
                        "id": 8,
                        "name": "IBUDONE",
                        "price": 180
                    }
                ]
            }
        },
        "non-prescription": {
            "analgesic": {
                "general": [
                    {
                        "id": 9,
                        "name": "Acetaminophen",
                        "price": 15
                    },
                    {
                        "id": 10,
                        "name": "Ibuprofen",
                        "price": 20
                    }
                ]
            },
            "antihistamine": {
                "antiallergic": [
                    {
                        "id": 11,
                        "name": "Loratadine",
                        "price": 12
                    },
                    {
                        "id": 12,
                        "name": "Desler M",
                        "price": 8
                    },
                    {
                        "id": 13,
                        "name": "Allegra",
                        "price": 21
                    },
                    {
                        "id": 14,
                        "name": "Fexofenadine",
                        "price": 18
                    }
                ]
            }
        }
    }

print ("***WELCOME***")

while True:
    option = int(input("Please write an option \n1 Catalog \n2 Buy \n3 Go back to the main menu \n4 Exit \n -> "))
    if option ==1:
        for prescription , typemed in medications.items():
            print (prescription)
            for body_part , especmed in typemed.items():
                print (body_part)
                for info,epecinfo in especmed.items():
                    print (info)
                    for secinfo in epecinfo: 
                        id = secinfo.get("id")
                        name = secinfo.get("name")
                        price = secinfo.get ("price")
                    print (f"""
                    Medication id : {id} 
                    Mediaction name : {name}
                    Medication price : {price} """)
    if option == 2: 
        client = {}
        customer_name = input("Please write your name -> ")
        customer_id = input ("Please write your id -> ")
        customer_selection = int(input ("Please write the product id that you want to buy -> "))
        client["customer_name"]=customer_name
        client["customer_id"]= customer_id
        client["customer_selection"]=customer_selection

        selection = None 

        while selection == None:
            for prescription , typemed in medications.items():
                for body_part , especmed in typemed.items():
                    for info,epecinfo in especmed.items():
                        for secinfo in epecinfo: 
                            if secinfo.get("id")== customer_selection:
                                selection = secinfo
                                break
            customer_selection = int(input("Please write a correct id: "))
            
        else: 
            print ("***RECEIPT***")
            for infoc,infocliente in client.items():
                print(infocliente)
            for selecprod,clientselec in selection.items():
                print (selecprod, clientselec)
            break
    elif option == 3:
        continue

    elif option == 4:
        break 

    else:
        option = int (input ("please write a correct option: "))

            
        








                
               

