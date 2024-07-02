n = 30
arr = []
cab = None
sig = None
disp = 0
dato = 0
"""
            for i in range(0, n-1):
                arr[i].sig(i + 1)
            arr[n-1].sig(-1)
            
"""
def insertar(dato):
    if disp != -1:
        arr[disp].info = dato
        if cab == -1 or dato < arr[cab].info:
            arr[disp].sig = cab
            cab = disp
            

        else:
            aux = cab
            while aux != -1 and dato > arr[aux].info:
                ant = aux
                aux = arr[aux].sig
            auxDisp = arr[disp].sig
            arr[disp].sig = arr[ant].sig
            arr[ant].sig = disp
        
        disp = auxDisp
            
            
            
def suprimir(dato):
    aux = cab
    if cab != -1:
        while aux != -1 and arr[aux].info != dato:
            ant = aux
            aux = arr[aux].sig
        if aux != -1:
            
            arr[ant].sig = arr[aux].sig
            
            arr[aux].sig = disp
            disp = aux
            
                
    else:
           