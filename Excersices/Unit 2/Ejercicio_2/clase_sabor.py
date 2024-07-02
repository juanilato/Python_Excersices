


class Sabor:
    def __init__(self, idSabor, ingredientes, nombreSabor):
        self.__idSabor = idSabor
        self.__ingredientes = ingredientes
        self.__nombreSabor = nombreSabor
        self.__contador = 0
    def __str__(self):
        cadena = str(self.__idSabor) + ": "
        cadena += self.__nombreSabor + " "
        return cadena
    def cuenta(self):
        self.__contador += 1
    def getContador(self):
        return self.__contador
    def __lt__(self, otro):
        return self.__contador > otro.__contador
    def getID(self):
        return self.__idSabor