import numpy as np
class pilaSecuencial:
    def __init__(self,xmax):
        self.___cola = np.empty(xmax,dtype=int)
        self.__max = xmax
        self.__tope = 0
    
    def vacia(self):
        return self.__tope == 0
    
    def llena(self):
        return self.__tope == self.__max
    
    def insertar(self, elemento):
        if self.llena():
            print("La cola está llena, no se puede insertar más elementos.")
            return
        else:
            self.___cola[self.__tope] = elemento
            self.__tope += 1
    
    def suprimir(self):
        if self.vacia():
            print("La cola está vacía, no hay elementos para suprimir.")
        else:
            self.___cola[self.__tope - 1]
            self.__tope -= 1
            return self.___cola[self.__tope]
           
    def recorrer(self):
        if self.vacia():
            print("La cola está vacía, no hay elementos para recorrer.")
            return
        else:
            for i in range(self.__tope - 1, -1, -1):
                print(self.___cola[i], end=" ")
    
    def factorial(self, x):
        res = 1
        num = x

        while x > 0:
            print(f"Apilando: {x}")
            pila.insertar(x)
            x -= 1
        print(f"{num}! = ",end= " ")
        while not self.vacia():
            n = self.suprimir()
            print(f"{n}",end=" * ")
            res *= n
        print(f"= {res}")

        print(f"\nEl factorial de {num} es: {res}")

if __name__ == "__main__":
    num = int(input("Ingrese el numero que quiera sacarle factorial: "))
    pila = pilaSecuencial(num)
    pila.factorial(num)
