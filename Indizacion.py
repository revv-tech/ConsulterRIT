import csv

#==================
#MANEJO DE ARCHIVOS
#==================
#E: El path del archivo, un string con formato de lista
#S: Ninguna
#D: Guarda el archivo
def guardar (archivo, strLista):
     fo = open(archivo, "w")
     fo.write(strLista)
     fo.close()


# E: La lista con las sublistas de cada instruccion
# S: Una lista
# D: lee la lista y elimina espacios en blanco
def eliminaEspacios(archivoListas):
    for row in archivoListas:
        if "" in row:
            while "" in row:
                row.remove("")

    return archivoListas


#E: El texto de un archivo
#S: Una lista de los elementos de las
#D: Lee el archivo, separa sus elementos y los almacena en una lista de sublistas

#LISTA => [[CODE],[AUTOR],[DESCRIPCION]]

def leer(archivo):

    lista = []
    fo = open(archivo,"r")
    reader = csv.reader(fo)
    for row in reader:
        print(row)
        segmento = row[0].split(" ")
        segmento += row[1:]
        lista.append(segmento)

    return lista
#E: El path del archivo
#S:Una lista
#D:lee un archivo y hace las validaciones para colocarlo en la lista
def cargarArchivo(archivo):
     strResultado = leer(archivo)
     if strResultado != "":
          return strResultado
     else:
          return []

#PRUEBA
nameFile = "prueba.txt"
print(cargarArchivo(nameFile))


