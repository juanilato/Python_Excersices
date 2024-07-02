
class Materia():
    def __init__(self, dni, nombreMateria, fecha, nota, aprobacion):
        self.__dni = dni
        self.__nombreMateria = nombreMateria
        self.__fecha = fecha
        self.__nota = nota
        self.__aprobacion = aprobacion
    def getDni(self):
        return self.__dni
    def getNota(self):
        return self.__nota
    def getFecha(self):
        return self.__fecha
    def getNombre(self):
        return self.__nombreMateria