from Pila import Pila

def calc_factorial(pila, numero):
    ele=1
    while numero>0:
        pila.apilar(numero)
        numero-=1
    
    while not pila.vacia():
        numero=pila.desapilar()
        ele*=numero
    
    print (ele)
    
if __name__=="__main__":
    numero=int(input("Ingresar el numero para calcular el factorial: "))
    pila=Pila(numero)
    calc_factorial(pila,numero)