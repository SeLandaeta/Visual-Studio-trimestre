from ast import Continue


def main(): 

    products = {

        "mobiles": {

            "Apple": [

                {

                    "id": 1,

                    "name": "iPhone 7",

                    "price": 300

                },

                {

                    "id": 2,

                    "name": "iPhone 8",

                    "price": 350

                },

                {

                    "id": 3,

                    "name": "iPhone Xr",

                    "price": 450

                },

                {

                    "id": 4,

                    "name": "iPhone Xs",

                    "price": 460

                },

                {

                    "id": 5,

                    "name": "iPhone 11",

                    "price": 900

                },

                {

                    "id": 6,

                    "name": "iPhone 12",

                    "price": 1100

                },

                {

                    "id": 7,

                    "name": "iPhone 13",

                    "price": 1300

                },

            ],

            "Samsung": [

                {

                    "id": 8,

                    "name": "Samsung Galaxy Beam",

                    "price": 150

                },

                {

                    "id": 9,

                    "name": "Samsung Galaxy S6",

                    "price": 200

                },

                {

                    "id": 10,

                    "name": "Samsung Galaxy S7",

                    "price": 300

                },

            ],

            "Xiaomi": [

                {

                    "id": 11,

                    "name": "Xiaomi Redmi Note 8",

                    "price": 250

                },

                {

                    "id": 12,

                    "name": "Xiaomi Redmi Note 8 Pro",

                    "price": 300

                },

            ]

        },

        "laptops": {

            "DELL": [

                {

                    "id": 13,

                    "name": "Dell Inspiron 15",

                    "price": 600

                },

                {

                    "id": 14,

                    "name": "Dell Latitude 14",

                    "price": 650

                },

            ],

            "MAC": [

                {

                    "id": 15,

                    "name": "MacBook Pro 13",

                    "price": 900

                },

                {

                    "id": 16,

                    "name": "MacBook M1",

                    "price": 1500

                },

            ]

        },

    }

    print ("$$$Bienvenido$$$")
    while True: 
        option = int(input ("Please select an option \n1 Catalog \n2 Buy \n3 Main menu \n4 Exit \n -> "))
        available_types = {1:"mobiles",2:"laptops"}
        if option == 1: 
            for brands, devices in products.items():
                for brand_name , product_list in devices.items():
                    for product in product_list: 
                        id = product.get("id")
                        name = product.get("name")
                        price = product.get("price")
                        print (f"""
                        id:{id} 
                        name:{name} 
                        price: {price}""")
        
        elif option == 2:
            client = {}
            customer_name = input("Please enter your name -> ")
            customer_id = input ("Please enter your id -> ")
            id_product =int( input ("Please enter the product id -> "))
            client["customer_name"] = customer_name
            client ["customer_id"] = customer_id
            client ["id_product"] = id_product

            product_selected = None 

            for brands, devices in products.items():
                for brand_name , product_list in devices.items():
                    for product in product_list: 
                        if product.get("id") == id_product:
                            product_selected = product
                            break
            if product_selected == None :
                print ("yout id selected is not founded ")
            else:
                print ("***REEIPT***")
                for key,values in client.items(): 
                    print (values)
                for key,value in product_selected.items():
                    print (key,value )
                break

            


     
                
            
           

        elif option == 3:
            continue
        else: 
            break




main()