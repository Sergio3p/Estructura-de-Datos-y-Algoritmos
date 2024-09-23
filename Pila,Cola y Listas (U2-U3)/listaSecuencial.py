import numpy as np

class listaSecuencial:
    def __init__(self,xmax):
        self.__lista = np.empty(xmax,dtype=int)
        self.__cant = 0
        self.__max = xmax
    
    def vacia(self):
        return self.__cant == 0

    def llena(self):
        return self.__cant == self.__max
    
    def insertar(self,pos,x):
        if self.llena():
            print("La lista está llena")
        elif 0 <= pos <= self.__cant+1:
            for i in range(self.__cant, pos-1, -1):
                self.__lista[i] = self.__lista[i-1]
            self.__lista[pos-1] = x
            self.__cant += 1
        else:
            print("Posición inválida")
    
    def suprimir(self, pos):
        if self.vacia():
            print("La lista está vacía")
        else:
            for i in range(pos - 1, self.__cant - 1):
                self.__lista[i] = self.__lista[i + 1]
            self.__lista[self.__cant - 1] = 0  # Corregido: asignar a self.__cant - 1
            self.__cant -= 1
            
    def recuperar(self,pos): #posición
        if self.vacia(): 
            print("La lista está vacía")
        elif 0 < pos < self.__cant+1:
            print(f"En la posición {pos} se encuentra: {self.__lista[pos-1]}")
        else:
            print("Posición inválida")

    def buscar(self,x): #elemento
        i = 0
        band = False
        while i < self.__cant and not band:
            if self.__lista[i] == x:
                print(f"El elemento se encuentra en la posición {i+1}")
                band = True
            i += 1
        if not band:
            print("El elemento no se encuentra en la lista")
        
    def primerElemento(self):
        if self.vacia():
            print("La lista está vacía")
        else:
             print(f"Primer elemento:{self.__lista[0]}")
    
    def ultimoElemento(self):
        if self.vacia():
            print("La lista está vacía")
        else:
             print(f"ultimo elemento: {self.__lista[self.__cant-1]}")
    
    def anterior(self,pos):
        if self.vacia():
            print("La lista está vacía")
        elif pos <= 0 or pos > self.__cant:
            print("Posición inválida")
        else:
             print(f"Posición anterior: {pos-1}")
    
    def siguiente(self, pos):
        if self.vacia():
            print("La lista está vacía")
        elif pos < 1 or pos >= self.__cant:
            print("Posición inválida")
        else:
             print(f"posición siguiente: {pos+1}")

    def recorrer(self):
        if self.vacia():
            print("La lista está vacía")
        else:
            print("Elementos de la lista:")
            for i in range(self.__cant):
                print(f"{self.__lista[i]}",end=" ")
            print("")
    
if __name__ == "__main__":
    lista_sec = listaSecuencial(4)
    lista_sec.insertar(1,2)
    lista_sec.buscar(2)
    lista_sec.insertar(2,1)
    lista_sec.insertar(3,3)
    lista_sec.insertar(5,3)
    lista_sec.recorrer()
    lista_sec.suprimir(1)
    lista_sec.recorrer()
    lista_sec.recuperar(2)
    lista_sec.buscar(3)
    lista_sec.buscar(4)
    lista_sec.primerElemento()
    lista_sec.ultimoElemento()
    lista_sec.siguiente(1)
    #lista_sec.siguiente(3)
    lista_sec.anterior(2)
    #lista_sec.anterior(1)

