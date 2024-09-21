import numpy as np
class pilaSecuencial:
    def __init__(self,xmax):
        self.__pila = np.empty(xmax, dtype=int)
        self.__max = xmax
        self.__tope = 0
    
    def vacia(self):
        return self.__tope == 0
    
    def llena(self):
        return self.__tope == self.__max
    
    def insertar(self,x):
        if self.llena():
            print("Pila llena")
        else:
            self.__pila[self.__tope] = x
            self.__tope += 1
         
    def suprimir(self):
        if self.vacia():
            print("La cola está vacía.")
        else:
            self.__tope -= 1
            return self.__pila[self.__tope]
            
    def tope(self):
        num = 0
        if not self.vacia():
            num = self.__pila[self.__tope - 1]
        else:
            num = 0
        return num
    
    def recorrer(self):
        if self.vacia():
            print("[]")
        else:
            print("[ ",end="")
            for i in range(self.__tope):
                print(self.__pila[i], end=" ")
            print("]")
    
def moverDisco(origen,destino):
    band = True
    if origen.vacia():
        print("No hay discos en la pila origen.")
        band = False
    elif not destino.vacia() and origen.tope() > destino.tope():
        print("No se puede mover un disco más grande sobre uno más pequeño.")
        band = False
    return band

def torresDeHanoi(p1,p2,p3,n):
    band1 = False
    dicc_pila= {1:p1,2:p2,3:p3}

    for i in range(n,-1,-1):
        p1.insertar(i)
    p1.recorrer()
    p2.recorrer()
    p3.recorrer()
    movimientos = 0

    while not p1.vacia() and p2.vacia() or not band1:
        origen = int(input("Ingrese la pila de origen: "))
        destino = int(input("Ingrese la pila de destino: "))

        pila_or = dicc_pila[origen]
        pila_des = dicc_pila[destino]

        band2 = moverDisco(pila_or,pila_des)

        if band2:
            disco = pila_or.suprimir()
            pila_des.insertar(disco)
            movimientos += 1
        
        print("Estado de las torres:")
        p1.recorrer()
        p2.recorrer()
        p3.recorrer()

        if p3.llena():
            print("Ganaste el juego!!!")
            print(f"cantidad de movimientos: {movimientos}")
            print(f"El mínimo de movimientos posibles es {2**n - 1}.")
            band1 = True

if __name__ == "__main__":
    n = int(input("Ingrese la cantidad de discos que utilizara en las torres: "))
    pila1 = pilaSecuencial(n)
    pila2 = pilaSecuencial(n)
    pila3 = pilaSecuencial(n)

    torresDeHanoi(pila1,pila2,pila3,n)