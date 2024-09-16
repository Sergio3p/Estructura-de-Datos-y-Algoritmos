class Nodo:
    def __init__(self,dato,sig=None):
        self.__dato = dato
        self.__sig = sig

    def get_dato(self):
        return self.__dato
    
    def get_sig(self):
        return self.__sig
    
    def set_sig(self, dato):
        self.__sig = dato

class PilaEncadenada:
    def __init__(self):
        self.__tope = None
        self.__cant_elementos = 0

    def vacia(self):
        return self.__cant_elementos == 0
    
    def insertar(self, x):
        nuevo = Nodo(x,self.__tope)
        self.__tope = nuevo
        self.__cant_elementos += 1
    
    def suprimir(self):
        if self.vacia():
            print("La pila está vacía.")
        else:
            aux = self.__tope #creamos una variable que contenga el tope para luego señalar al siguiente elemento que le sigue
            self.__tope = aux.get_sig() #Obtenemos el siguiente con el aux y guardaremos este mismo en el tope
            self.__cant_elementos-=1

    def recorrer(self):
        if self.vacia():
            print("La pila está vacía.")
        else:
            aux = self.__tope
            while aux is not None:
                print(aux.get_dato(), end=" -> ")
                aux = aux.get_sig()
            print("")

if __name__=="__main__":
    pila = PilaEncadenada()
    pila.insertar(5)
    pila.insertar(10)
    pila.insertar(15)
    pila.insertar(20)
    pila.recorrer()
    pila.suprimir()
    pila.recorrer()