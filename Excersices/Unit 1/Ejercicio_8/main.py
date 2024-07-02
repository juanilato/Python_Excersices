from clase_conjunto import Conjunto
from clase_menu import Menu


if __name__ == "__main__":
    arreglo1 = [1,2,3,4]
    arreglo2 = [4,3,2,1]
    
    
    conjunto1 = Conjunto(arreglo1)
    conjunto2 = Conjunto(arreglo2)
    
    
    
    opciones = ["Unir conjuntos", "Restar conjuntos ", "Verifica igualdad"]
    cantidad = 3
    menu = Menu(cantidad)
    menu.IngresaOpcion(opciones)
    
    menu.Muestra()
    op = int(input("Ingrese opcion "))
    
    while op != (cantidad + 1):
        if op == 1:
            conjunto3 = conjunto1 + conjunto2 
            conjunto3.muestra()
        elif op == 2:
            conjunto3 = conjunto1 - conjunto2
            conjunto3.muestra()
        elif op == 3:
            if conjunto1 == conjunto2:
                print("Si son iguales")
            else: 
                print("No son iguales")        
        else:
            print("Ingreso opción incorrecta")
        menu.Muestra()
        op = int(input("Ingrese opcion "))
        
    