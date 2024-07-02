class ViajeroFrecuente(): 
    #Método constructor
    def __init__(self, numviaj:int, dni:int, nombre:str, apellido:str, millas_acum:int):
        self.__num_viajero = numviaj
        self.__dni = dni
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millas_acum = millas_acum
    
    def cantidadTotalMillas(self):
        return self.__millas_acum
    
    def canjearMillas(self, num):
        if num <= self.__millas_acum:
            self.__millas_acum = self.__millas_acum - num 
            print("Sus millas han sido canjeadas con exito")
            print("nuevas millas son: ", self.__millas_acum)
        else:
            print("No se ha conseguido canjear las millas /n")
            print("Millas ingresadas superan a las millas acumuladas /n")
        return self.cantidadTotalMillas()
    
    def MostrarDatos(self):
        print(f"Numero de viajero:{self.__num_viajero}\n{self.__apellido} {self.__nombre}\n Tiene {self.__millas_acum} millas acumuladas .\n Su dni es: {self.__dni}")
    
    def getNumViajero(self):
        return int(self.__num_viajero)
    
    def __add__(self, num):
        return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum + num)
    
    def __gt__(self, otro):
        return self.cantidadTotalMillas() > otro.cantidadTotalMillas()
    
    def __sub__(self, num):
        return ViajeroFrecuente(self.__num_viajero, self.__dni, self.__nombre, self.__apellido, self.__millas_acum - num)
    