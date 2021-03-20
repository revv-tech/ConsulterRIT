#Documentos

class Documents:

    def __init__(self,listDoc,docID,path):

        #Lista de Terminos del Documento
        self.listDoc = listDoc
        #Numero consecutivo unico generado aleatoriamente
        self.docID = docID
        #Ruta del Documento
        self.path = path
        #Descripcion
        self.descrip = []
        #Numero de terminos distintos del documento
        self.cantTerms = 0
        #Longitud del Documento (Suma de las frecuencias de todos los terminos del documento
        self.longitud = 0
        #Lista de Vectores (Orden Alfabetico)
        self.pares = []

        
