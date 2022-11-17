import json

crearjson={
  "book": [
      {"title":"Harry Potter",
       "cover": "JK rowling",
       "year": "2000",
       "pages": "200"
      },
      {"title":"Harry Potter 2",
       "cover": "JK rowling",
       "year": "2005",
       "pages": "200"
      },
       {"title":"Harry Potter 3",
       "cover": "JK rowling",
       "year": "2010",
       "pages": "200"
      },
       {"title":"Harry Potter 4",
       "cover": "JK rowling",
       "year": "2015",
       "pages": "200"
      }
  ]
}
with open("crearjson","w") as file:
    json.dump(crearjson,file)
#Cogemos el archivo json creado
# y lo cargamos para asignarlo a una variable
with open("crearjson","r") as patata:
    result = json.load(patata)
    #Lo que hemos cargado en file lo pasamos
    # a una variable para poderlo imprimier
    print(patata)
    #Aqui indetamos el resultado
    resultindent=(json.dumps(result, indent=2))
    print(resultindent)