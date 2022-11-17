import csv

def escribircsv():
    #INPUTS PARA LA LISTA
    nombre = input("nombre: ")
    apellido = input("apellido: ")
    edad = input("edad: ")
    #LISTA CONTENIENDO DOS LISTAS: UNA CON EL NOMBRE DE LAS COLUMNAS Y OTRA CON LOS VALORES
    data = [["Name", "Surname", "Age"], [nombre, apellido, edad ]]

    with open('archivo.csv', 'w', newline='') as file:#ABRE EL ARCHIVO  SI EXISTE, SI NO EXISTE LO CREA Y LO GUARDA EN LA VARIABLE FILE
        writer = csv.writer(file, quoting=csv.QUOTE_ALL,delimiter=',') #OBJETO WRITER DEL MODULO CSV QUE RECIVE UN PARAMETRO CON EL ARCHIVO Y EL SEGUNDO INDICA QUE DELIMITADOR SE USARA
        writer.writerows(data) #METODO DEL OBJETO WRITER QUE RECIVE EL CONTENIDO A ESCRIBIR


def leercsv():
    with open('archivo.csv', newline='') as File: #IGUAL QUE ESCRIBIENDO  
        reader = csv.reader(File) #OBJETO READER DE CSV
        for row in reader: #BUCLE QUE RECORRE EL OBJETO READER Y LO IMPRIME ( READER CONTIENE UNA LISTA)
            print(row)
            #print(type(row))


escribircsv()
leercsv()