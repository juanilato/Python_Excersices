

class Recepcionista:
    def __init__(self, tiempo_atencion_max):
        self.__acum = 0
        self.__cant = 0
        self.__tiempo_atencion = 0
        self.__tiempo_atencion_max = tiempo_atencion_max
        

        
    def getTiempo(self):
        return self.__tiempo_atencion
    
    def setTiempo(self):
        self.__tiempo_atencion = self.__tiempo_atencion_max
        
    def resetTiempo(self):
         self.__tiempo_atencion = 0
        
    def descontarTiempo(self):
        self.__tiempo_atencion -= 1
        
    def sumarDato(self, dato):
        self.__acum += dato
        
        
    def contarCant(self):
        self.__cant += 1
        
    def getCant(self):
        return self.__cant
    
    def calculaTiempo(self):
        return self.__acum / self.__cant