class Nodo:
    def __init__(self, dato,sig = None):
        self.__dato = dato
        self.__sig = sig
    
    def getSiguiente(self):
        return self.__sig

    def getDato(self):
        return self.__dato
    
    def setSiguiente(self, dato):
        self.__sig = dato

class colaEncadenada:
    def __init__(self):
        self.__cant = 0
        self.__ul = None
        self.__pr = None
    
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,dato):
        nuevo = Nodo(dato)
        if self.vacia():
            self.__pr = nuevo
        else:
            self.__ul.setSiguiente(nuevo)
        self.__ul = nuevo
        self.__cant += 1
    
    def suprimir(self):
        if self.vacia():
            print("La cola está vacía")
            return
        else:
            dato = self.__pr.getDato()
            self.__pr = self.__pr.getSiguiente()
            self.__cant -= 1
            if self.vacia():
                self.__ul = None
            return dato
        
    def recorrer(self):
        if self.vacia():
            print("La cola está vacía")
        else:
            aux = self.__pr
            while aux is not None:
                print(aux.getDato(), end = " ")
                aux = aux.getSiguiente()
            print()

if __name__=="__main__":
    cola = colaEncadenada()
    cola.insertar(5)
    cola.insertar(10)
    cola.insertar(15)
    cola.insertar(20)
    cola.recorrer()
    print(f"{cola.suprimir()}")
    cola.recorrer()