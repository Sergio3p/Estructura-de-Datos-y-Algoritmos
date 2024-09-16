import numpy as np

class colaSecuencial:
    def __init__(self,xmax):
        self.__max = xmax
        self.__pr = 0
        self.__ul = 0
        self.__cant_elementos = 0
        self.__lista = np.empty(xmax, dtype=int)
    
    def vacia(self):
        return self.__cant_elementos == 0
    
    def llena(self):
        return self.__cant_elementos == self.__max
    
    def insertar(self,x):
        if self.llena():
            raise Exception('La cola está llena')
        self.__lista[self.__ul] = x
        self.__ul = (self.__ul + 1) % self.__max
        self.__cant_elementos += 1
    
    def suprimir(self):
        if self.vacia():
            raise Exception('La cola está vacía')
        x = self.__lista[self.__pr]
        self.__pr = (self.__pr + 1) % self.__max
        self.__cant_elementos -= 1
        return x

    def recorrer(self):
        if self.vacia():
            print("No hay elementos en la cola\n")
        else:
            i = self.__pr #obtenemos la primera posicion
            j = 0 # esto no permite iterar por la cantidad de elementos
            while j < self.__cant_elementos:
                print(round(self.__lista[i]),end=" ")
                j+=1
                i = (i+1) % self.__max #movimiento cirular para obtener la siguiente posicion
        print("")
if __name__=="__main__":
    cola = colaSecuencial(5)
    cola.insertar(5)
    cola.insertar(10)
    cola.insertar(15)
    cola.insertar(20)
    cola.recorrer()
    cola.suprimir()
    cola.recorrer()