from unicodedata import name


vinyls = {
  "1": { "name": "Cuando Los Acéfalos Predominan",
        "author": "Rawayana",
        "release_year": "2021",
        "stock": 1000,
        "sold": 0,
        "price": 10,
      },
  "2": { "name": "Notes on a Conditional Form",
        "author": "The 1975",
        "release_year": "2020",
        "stock": 1200,
        "sold": 0,
        "price": 20,
      },
  "3": { "name": "Call Me If You Get Lost",
        "author": "Tyler, the Creator",
        "release_year": "2021",
        "stock": 900,
        "sold": 0,
        "price": 30,
      },
  "4": { "name": "El Mal Querer",
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
modulos_tienda = True 
Comprastotal=[]

while modulos_tienda : 
    modulo = input ("Porfavor indique a que modulo desea acceder: \n1-Catalogo \n2 Inventario \n-> ") 
    while modulo == "1": 
      lista_nombres = []
      for id , discos  in vinyls.items(): 
            print (f""" disco numero : {id}
            Nombre del disco : {discos["name"]}
            Autor del disco:{discos["author"]}
            Año de lanzamiento: {discos["release_year"]}
            Disponibilidad: {discos["stock"]}
            Precio: {discos["price"]}
            Unidades vendidas: {discos["sold"]}""")
          
    while  not (modulo == "1" or modulo == "2"):
      modulo = input ("Por favor ingrese un modulo adecuado ")
    
