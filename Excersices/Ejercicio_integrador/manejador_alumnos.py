import numpy as np
from clase_alumno import Alumno
import csv

class ManejadorAlumnos():
    def __init__(self):
        self.__arreglo = np.array([], dtype = Alumno)
    
    def muestra(self):
        for alumno in self.__arreglo:
            print(alumno)
    def carga(self):
        archivo = open("alumnos.csv")
        reader = csv.reader(archivo, delimiter = ";")
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                alumno = Alumno(int(fila[0]),fila[1],fila[2],fila[3],int(fila[4]))
                self.__arreglo = np.append(self.__arreglo, alumno)
        archivo.close()
    
    def buscaDatos(self, dni):
        validador = False
        i = 0
        while ((validador == False) and (i < len(self.__arreglo))):
            dni_alu = self.__arreglo[i].getDni()
            if (dni_alu == dni):
                validador = True
            else:
                i += 1
        if validador:
            return self.__arreglo[i]
        
    
    def ordenar(self):
        self.__arreglo.sort()