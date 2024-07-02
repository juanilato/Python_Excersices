from clase_materia import Materia
import csv

class ManejadorMaterias():
    
    def __init__(self):
        self.__lista = []
    def carga(self):
        archivo = open("materiasAprobadas.csv")
        reader = csv.reader(archivo, delimiter =";")
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                materia = Materia(int(fila[0]),fila[1],fila[2],int(fila[3]),fila[4])
                self.__lista.append(materia)
        archivo.close()
    def calculoProm(self, dni):
        promSinA = 0
        promConA = 0
        contadorSinA = 0
        contadorConA = 0
        for materia in self.__lista:
            dniD = materia.getDni()
            if dniD == dni:
                nota = materia.getNota()
                if nota < 4:
                    promConA += nota
                    contadorConA += 1 
                else:
                    contadorConA += 1 
                    promConA += nota
                    
                    contadorSinA +=1
                    promSinA += nota
                    
        print(f"Promedio del alumno: {dni}")
        print(f"Con aplazos {promConA/contadorConA}")
        print(f"Sin aplazos {promSinA/contadorSinA}")
    def devolverDatos(self, materia):
        listaMateriaSolicitada = []
        for objeto in self.__lista:
            materia_nombre = objeto.getNombre()
            materia_nota = objeto.getNota()
            if materia_nombre == materia and materia_nota >= 7:
                listaMateriaSolicitada.append(objeto)
        return listaMateriaSolicitada
    
