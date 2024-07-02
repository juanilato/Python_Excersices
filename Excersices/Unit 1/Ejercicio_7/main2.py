from ViajeroFrecuente import ViajeroFrecuente
import csv

if __name__ == "__main__":
    listaViajeros = []
    archivo = open("viajeros.csv")
    reader = csv.reader(archivo, delimiter = ",")
    for fila in reader: 
        viajero = ViajeroFrecuente(fila[0], int(fila[1]), fila[2],fila[3], int(fila[4]))
        listaViajeros.append(viajero)
    archivo.close()
    """
    Determinar el/los viajero/s con mayor cantidad de millas acumuladas. Para distinguir entre dos objetos 
    ViajeroFrecuente cuál posee mayor cantidad de millas acumuladas, sobrecargue el operador relacional mayor
    (> o  __gt__ en python).
    """
    
    #lista de viajeros con la mayor cantidad de millas
    viajeroMaximo = []
    
    #Busqueda numero máximo de millas
    numeroMillasMax = 0
    
    for objeto in listaViajeros:
        if objeto.cantidadTotalMillas() > numeroMillasMax:
            numeroMillasMax = objeto.cantidadTotalMillas()
    
    print ("Viajeros que poseen la mayor cantidad de millas: \n")
    
    #compara si es el mismo número
    for objeto in listaViajeros:
        if numeroMillasMax == objeto.cantidadTotalMillas():
            objeto.MostrarDatos()
            viajeroMaximo.append(objeto)
    

    """
    Acumular millas usando la sobrecarga del operador binario suma(+), 
    obteniendo como resultado de la suma 
    una instancia de la clase ViajeroFrecuente. 
    Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, 
    la función de acumular millas se resuelve de la siguiente forma v = v + 100.
    """
    listaViajeros[1] = listaViajeros[1] + 100
    listaViajeros[1].MostrarDatos()
    
    
    """
    Canjear millas usando la sobrecarga del operador binario resta(-),obteniendo como 
    resultado de la resta una instancia de la clase ViajeroFrecuente. 
    Por ejemplo, sea v una instancia de la clase ViajeroFrecuente, 
    la función de canjear millas se resuelve de la siguiente forma v = v - 100.
    """
     
    listaViajeros[1] = listaViajeros[1] - 150
    listaViajeros[1].MostrarDatos() 