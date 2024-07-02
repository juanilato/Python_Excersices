from Pila import Pila

def ConvertirDec_Bin(numero_dec, pila):
    
    while numero_dec >= 2:
        resto = numero_dec % 2
        
        if resto != 0:
            numero_dec -= 1
                 
        numero_dec = numero_dec / 2
        
        pila.apilar(resto)
    
    pila.apilar(int(numero_dec))
    
if __name__=="__main__":
    pila=Pila(10)
    num=int(input("Ingresar el numero para calcular su valor en binario: "))
    ConvertirDec_Bin(num,pila)
    pila.print()
    
    