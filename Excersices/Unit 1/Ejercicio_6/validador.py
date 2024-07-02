
def validaViajero(num_viajero, listaViajeros):
    validador = False
    i = 0
    while ((validador == False) & (i < len(listaViajeros))):
        if (listaViajeros[i].getNumViajero() == num_viajero):
            validador = True
        else: 
            i = i + 1
    if validador == False:
        return -1
    else: 
        return i

