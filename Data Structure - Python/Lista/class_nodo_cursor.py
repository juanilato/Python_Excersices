


class Nodo:
    def __init__(self, sig = 0, info = 0):
        self.__sig = sig
        self.__info = info
        
    def sig(self, sig):
        self.__sig = sig
        
    def info(self, dato):
        self.__info = dato
        
    def getInfo(self):
        return self.__info
    
    def getSig(self):
        return self.__sig