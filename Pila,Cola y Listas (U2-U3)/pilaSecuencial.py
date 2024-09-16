import numpy as np
class pilaSecuencial:
    def __init__(self,xmax):
        self.__tope = 0
        self.__max = xmax
        self.__items = np.empty(xmax,dtype="int")
        
    def vacia(self):
        return self.__tope == 0    
    
    def llena(self): #parcial
        return self.__tope == self.__max
    
    def insertar(self,x):
        if not self.llena():
            self.__items[self.__tope] = x
            self.__tope += 1
        else:
            print("La pila está llena")

    def suprimir(self):
        if not self.vacia():
            self.__items[self.__tope - 1] = 0
            self.__tope -= 1
        else:
            print("La pila está vacía")
            
    def recorrer(self):
        for i in range(self.__tope-1,-1,-1):
            print(self.__items[i], end=" ")  
        print("")
    
if __name__=="__main__":
    pila = pilaSecuencial(5)
    pila.insertar(5)
    pila.insertar(10)
    pila.insertar(15)
    pila.insertar(20)
    pila.recorrer()
    pila.suprimir()
    pila.recorrer()