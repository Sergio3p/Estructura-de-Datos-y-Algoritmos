class Nodo:
    def __init__(self, dato, sig = None):
        self.__dato = dato
        self.__sig = sig
    
    def get_dato(self):
        return self.__dato
    
    def get_sig(self):
        return self.__sig
    
    def set_sig(self,dato):
        self.__sig = dato
    
class listaEncadenada:
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, pos, x):
        if pos < 1 or pos > self.__cant + 1:
            print("posición invalida")
        else:
            nuevo = Nodo(x)
            if pos == 1:
                nuevo.set_sig(self.__cabeza)
                self.__cabeza = nuevo
            else:
                aux = self.__cabeza
                for _ in range(pos - 2):  # Ajuste en el rango
                    aux = aux.get_sig()
                
                nuevo.set_sig(aux.get_sig())
                aux.set_sig(nuevo)
            self.__cant += 1  # Aumentar el contador al insertar
    
    def suprimir(self, pos):
        if self.vacia() or pos < 1 or pos > self.__cant:
            print("Posición inválida o lista vacía")
        else:
            if pos == 1:
                aux = self.__cabeza.get_dato()
                self.__cabeza = self.__cabeza.get_sig()
            else:
                aux = self.__cabeza
                for _ in range(pos - 2):  # Ajuste en el rango
                    aux = aux.get_sig()

                suprimir = aux.get_sig()
                valor = suprimir.get_dato()
                aux.set_sig(suprimir.get_sig())
            self.__cant -= 1  # Disminuir el contador al eliminar
    
    def recuperar(self, pos):
        if self.vacia() or pos < 1 or pos > self.__cant:
            print("Posición inválida o lista vacía \n")
        else:
            aux = self.__cabeza
            for _ in range(pos - 1):
                aux = aux.get_sig()
        
        if aux is not None:
            print("El dato en la posición", pos, "es:", aux.get_dato())
        else:
            print("Posición inválida \n")
    
    def buscar(self, x):
        band = False
        if self.vacia():
            print("La lista está vacía \n")
        else:
            aux = self.__cabeza
            pos = 1
            while aux is not None and band is False:
                if aux.get_dato() == x:
                    print("El dato", x, "se encuentra en la posición", pos)
                    band = True
                aux = aux.get_sig()
                pos += 1
            if not band:
                print("El dato", x, "no se encuentra en la lista \n")

    def recorrer(self):        
        if self.vacia():
            print("La lista está vacía \n")
        else:
            aux = self.__cabeza
            while aux is not None:
                print(aux.get_dato(), end=" -> ")
                aux = aux.get_sig()
            print("")
    
    def primerElemento(self):
        if self.vacia():
            print("La lista está vacía \n")
        else:
            print("El primer elemento de la lista es:", self.__cabeza.get_dato())
    
    def ultimoElemento(self):
        if self.vacia():
            print("La lista está vacía \n")
        else:
            aux = self.__cabeza
            while aux.get_sig() is not None:
                aux = aux.get_sig()
            print("El último elemento de la lista es:", aux.get_dato())
    
    def siguiente(self, pos):
        if 1 <= pos < self.__cant:  # Cambiar a self.__cant
            print(f"Siguiente posición: {pos+1}")
        else:
            print("La posición ingresada no tiene una siguiente\n")

    def anterior(self, pos):
        if 1 < pos <= self.__cant:  # Cambiar a self.__cant
            print(f"Anterior posición: {pos-1}")
        else:
            print("La posición ingresada no tiene una anterior\n")

if __name__ == "__main__":
    lista_enc = listaEncadenada()
    lista_enc.insertar(1, 1)
    lista_enc.insertar(2, 2)
    lista_enc.insertar(3, 3)
    lista_enc.recorrer()
    lista_enc.suprimir(2)
    lista_enc.recorrer()
