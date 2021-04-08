from  Consulta import *
from Inspeccion import *

def menu():
    print("----------------------------------------------------------------------------------------------------\n")
    print("1: Ingresar consulta\n")
    print("2: Herramienta Inspeccion\n")
    print("3: Indexar\n")
    print("----------------------------------------------------------------------------------------------------\n")
    n = int(input("Ingresar n: "))
    if n == 1:
        menuConsulta()
    elif n == 2:
        return menuHerramientaInsp()
    elif n == 3:
        directoryRunner()
        return menu()
    else:
        return menu()

def menuConsulta():
    print("----------------------------------------------------------------------------------------------------\n")
    print("                                               CONSULTA\n")
    print("----------------------------------------------------------------------------------------------------\n")
    indice = str(input("Ingresar ruta al directorio: "))
    print("\n")
    numDocs = int(input("Cantidad de Documentos: "))
    print("\n")
    resultado = str(input("Ingresar nombre de Archivos resultado: "))
    print("\n")
    consulta = str(input("Ingresar consulta: ")).lower()
    dict = sortDict(getSimDQ(consulta))
    print("----------------------------------------------------------------------------------------------------")
    createConsultas(dict, numDocs, resultado, consulta)
    print("Archiivos creados\n")
    return menu()


def menuHerramientaInsp():
    print("----------------------------------------------------------------------------------------------------\n")
    print("                                               INSPECCION\n")
    print("----------------------------------------------------------------------------------------------------\n")
    print("1: Termino")
    print("2: Documento")
    print("----------------------------------------------------------------------------------------------------")
    n = int(input("Ingresar opcion: "))
    if n == 1:
        term = input("Ingrese el termino a buscar: ")
        printTerms(term)
        print("\n")
        return menu()
    elif n == 2:
        doc = input("Ingrese el documento a buscar: ")
        printDoc(doc)
        print("\n")
        return menu()

try :
    jsonReader()
except(FileNotFoundError):
    print("Archivos no estan creados")
menu()