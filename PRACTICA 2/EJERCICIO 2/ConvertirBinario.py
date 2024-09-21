import numpy as np

class PilaSecuencial:
    def __init__(self,xmax):
        self.__pila = np.zeros(xmax, dtype=int)
        self.__cant = 0
        self.__max = xmax
    
    def vacia(self):
        return self.__cant == 0
    
    def llena(self):
        return self.__cant == self.__max
    
    def insertar(self,x):
        if self.llena():
            print("La pila está llena")
        else:
            self.__pila[self.__cant] = x
            self.__cant += 1
    
    def suprimir(self):
        if self.vacia():
            print("La pila está vacía")
        else:
            self.__cant -= 1
            return self.__pila[self.__cant]
    
    def recorrer(self):
        if self.vacia():
            print("La pila está vacía")
        else:
            for i in range(self.__cant-1, -1, -1):
                print(self.__pila[i], end=" ")
            print()
        
    def decimalABinario(self,x):
        while 0 < x:
            resto = x % 2
            self.insertar(resto)
            x = x // 2
        self.recorrer()

if __name__ == "__main__":
    pila = PilaSecuencial(8)
    pila.decimalABinario(4)

    
