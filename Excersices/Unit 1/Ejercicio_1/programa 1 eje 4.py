# -*- coding: utf-8 -*-
"""
    4- a) Leer de un archivo separado por comas 10 direcciones de email,
    crear las cuentas correspondientes, solo para las direcciones válidas,
    para las no válidas, mostrar mensaje de error indicando la dirección de email incorrecta.  
    b) Ingresar un dominio e indicar cuántos objetos de la clase Email, tienen dominio igual 
    al ingresado. 
    c) Construya el diagrama de secuencia correspondiente.
"""
import csv
from clase_email import Email

if __name__=="__main__":
    archivo = open('Emails.csv')
    reader = csv.reader(archivo, delimiter=',')
    emails = [] 
    for fila in reader:
        for elemento in fila:     
            correo = Email(None, None, None, None)
            if correo.crearCuenta(elemento)!= -1:
                emails.append(correo)
                print(f"Correo cargado correctamente: {elemento} \n")
            else:
                print(f"Correo Invalido: {elemento}\n")
    archivo.close()
    i = 0
    dominio = input("Ingrese un dominio a buscar ")
    
    
    
    for correo in emails:        
        if correo.getDominio() == dominio:
            i = i + 1
    
    print(f"Cantidad de dominios igual al ingresado fue: {i}")
    
    
