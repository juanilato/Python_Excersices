import csv
from clase_sabor import Sabor


class ManejaSabores:
    def __init__(self):
        self.__sabores = []
        self.__listaMuestra = []
    def cargar(self):
        archivo = open("sabores.csv", encoding = "utf-8")
        reader = csv.reader(archivo, delimiter = ";")
        i = 1
        for fila in reader:
            sabor = Sabor(i, str(fila[0]), str(fila[1]))
            i += 1
            self.__sabores.append(sabor)
            self.__listaMuestra.append(sabor)
    def busca(self, idSabor):
        i = 0
        while i < len(self.__sabores) and idSabor != self.__sabores[i].getID():    
            i += 1
        if i < len(self.__sabores):
            band = True
        else:
            band = False
        if band:
            return self.__sabores[i]
    
    def contarSabor(self, idSabor):
        i = 0
        while i < len(self.__sabores) and idSabor != self.__sabores[i].getID():    
            i += 1
        if i < len(self.__sabores):
            band = True
        else:
            band = False
        if band:
            self.__sabores[i].cuenta()
        
    def ordena(self):
        self.__sabores.sort()
        
    def muestraContador(self):
        for i in range(0,5):
            if self.__sabores[i].getContador() > 0:
                print("Para el sabor: " + str(self.__sabores[i]) + "Cantidad: " + str(self.__sabores[i].getContador()))
    
        
    def muestra(self):
        for sabor in self.__listaMuestra:
            print(sabor)