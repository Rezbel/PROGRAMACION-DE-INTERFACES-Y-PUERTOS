
archivo = open("../Unidad 3/Archivos/ejemplo.csv", "w")

listaNombre = [
    ["Clemente",26],
    ["Cristobal",17],
    ["Ana",5],
    ["Rene",30],
    ["Orozco",8],
    ["Jorge",72],
    ["Aquino",13],
    ["Badillo",65],
    ["Segoviano",71],
    ["Salazar",9],
    ["Eduardo",50],
    ["Natalia",18],
    ["Rodrigo",55],
    ["Miguel",31],
    ["Amando",69],
    ["Raul",14],
    ["Lexiss",3],
    ["Mariana",33],
    ["Angel",10],
    ["Emmanuel",51],
    ["Isaac",70],
    ["Sergio",85],
    ["Paniagua",82]
]

print(listaNombre)

for datosNombre in listaNombre:
    for dato in datosNombre:
        archivo.write(str(dato) + ",")
    archivo.write("\n")

archivo.flush()
archivo.close()