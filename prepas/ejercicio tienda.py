vinyls = {
  "1": {"name": "Cuando Los Acéfalos Predominan",
        "author": "Rawayana",
        "release_year": "2021",
        "stock": 1000,
        "sold": 0,
        "price": 10,
      },
  "2": {"name": "Notes on a Conditional Form",
        "author": "The 1975",
        "release_year": "2020",
        "stock": 1200,
        "sold": 0,
        "price": 20,
      },
  "3": {"name": "Call Me If You Get Lost",
        "author": "Tyler, the Creator",
        "release_year": "2021",
        "stock": 900,
        "sold": 0,
        "price": 30,
      },
  "4": {"name": "El Mal Querer",
        "author": "Rosalía",
        "release_year": "2018",
        "stock": 980,
        "sold": 0,
        "price": 40,
      },
  "5": { "name": "The Dark Side of the Moon",
        "author": "Pink Floyd",
        "release_year": "1973",
        "stock": 500,
        "sold": 0,
        "price": 50,
      },
}

programa = True 
while programa: 
    modulo = input("What module do you want to see: \n1 Catalog \n2 Buy \n3 Sells \n-> ")
    while modulo == "1":
        lista_nombres = []
        for id, discos  in vinyls.items():
                        print (f""" 
                         disco:{id}
                        Record name : {discos["name"]}
                        Record Author : {discos["author"]}
                        Record release year: {discos["release_year"]}
                        Our stock : {discos["stock"]}
                        Price : {discos["price"]} '""" )
                        lista_nombres.append(discos["name"])

        nombreDisco = input("Ingrese el nombre del disco: ")
        while not (nombreDisco in lista_nombres):
          nombreDisco = input("Ingrese un nombre valido: ")
      
        idDisco = str(lista_nombres.index(nombreDisco) + 1)

        print(f"""
            El Disco que seleccionó fue el disco {idDisco}:
            Nombre: {vinyls[idDisco]["name"]}
            Autor: {vinyls[idDisco]["author"]}
            Año de lanzamiento: {vinyls[idDisco]["release_year"]}
            Stock: {vinyls[idDisco]["stock"]}
            Precio: {vinyls[idDisco]["price"]}
            Cantidad de ventas: {vinyls[idDisco]["sold"]}
        """)
        break



       

    
