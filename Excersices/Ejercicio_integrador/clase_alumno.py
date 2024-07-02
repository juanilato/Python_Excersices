

class Alumno():
    def __init__(self, dni, apellido, nombre, carrera, anio):
        self.__dni = dni
        self.__apellido = apellido
        self.__nombre = nombre
        self.__carrera = carrera
        self.__anio = anio
    def getDni(self):
        return self.__dni
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getAnioCursa(self):
        return self.__anio
    def __str__(self):
        return f"{self.__anio}  {self.__apellido}   {self.__nombre}"
    
    def __lt__(self, otro):
        if self.__anio == otro.__anio:
            return self.__apellido < otro.__apellido
        else:
            return self.__anio < otro.__anio
            
    