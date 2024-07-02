class Email():
    __identificacion: str
    __dominio: str
    __tipoDominio: str
    __contraseña: str
    #constructor
    def __init__(self, identificacion, dominio, tipoDominio, contraseña):
        self.__identificacion=identificacion
        self.__dominio=dominio
        self.__tipoDominio=tipoDominio
        self.__contraseña=contraseña
    #Construye una dirección e-mail con los valores de los atributos de Email
    def retornaEmail(self):
        return (self.__identificacion + "@" + self.__dominio + "." + self.__tipoDominio)
    #Retorna el dominio.
    def getDominio(self):
        return self.__dominio
    #Retorna la contraseña
    def getContraseña(self):
        return self.__contraseña
    #Realiza cambio de contraseña vieja por una nueva
    def cambioContraseña(self, antigua, nueva):
        if self.__contraseña==antigua:
            self.__contraseña = nueva
            return 0
        else: 
            return -1
    #Crea una cuenta a partir de una dirección de correo que recibe como parámetro.
    def crearCuenta(self,correo):
        if "@" in correo and "." in correo:
            nombre, dominio_tipo = correo.split("@")
            if "." in dominio_tipo:
                dominio, tipoDominio = dominio_tipo.split(".")
                self.__identificacion = nombre
                self.__dominio = dominio
                self.__tipoDominio = tipoDominio
                self.__contraseña = ""
                return 1
        return -1
        return 
        
        
        