import numpy as np

class listaSecuencial:
    def __init__(self, xmax):
        self.__lista = np.empty(xmax, dtype=int)
        self.__cant = 0
        self.__max = xmax
    
    def vacia(self):
        return self.__cant == 0

    def llena(self):
        return self.__cant == self.__max
    
    def insertar(self, x):
        if self.llena():
            print("Error: La lista está llena.")
            return

        # Encuentra la posición correcta para insertar el nuevo elemento
        pos = 0
        while pos < self.__cant and self.__lista[pos] <= x:
            pos += 1

        # Mueve los elementos para hacer espacio para el nuevo
        for i in range(self.__cant, pos, -1):
            self.__lista[i] = self.__lista[i - 1]

        # Inserta el nuevo elemento
        self.__lista[pos] = x
        self.__cant += 1
    
    def suprimir(self, pos):
        if self.vacia():
            print("La lista está vacía")
            return
        
        if pos < 1 or pos > self.__cant:
            print("Posición inválida")
            return

        for i in range(pos - 1, self.__cant - 1):
            self.__lista[i] = self.__lista[i + 1]
        self.__lista[self.__cant - 1] = 0  # Corregido: asignar a self.__cant - 1
        self.__cant -= 1
            
    def recuperar(self, pos):  # posición
        if self.vacia(): 
            print("La lista está vacía")
        elif 0 < pos < self.__cant + 1:
            print(f"En la posición {pos} se encuentra: {self.__lista[pos - 1]}")
        else:
            print("Posición inválida")

    # Buscar un elemento con búsqueda binaria
    def buscar(self, x):
        inicio = 0
        fin = self.__cant - 1  # __cant representa el número de elementos, por eso restamos 1 para obtener el último índice
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self.__lista[medio] == x:
                return medio + 1  # Retorna la posición (índice + 1)
            elif self.__lista[medio] < x:
                inicio = medio + 1
            else:
                fin = medio - 1
        return None  # Si no lo encuentra, devuelve None
        
    def primerElemento(self):
        if self.vacia():
            print("La lista está vacía")
        else:
             print(f"Primer elemento: {self.__lista[0]}")
    
    def ultimoElemento(self):
        if self.vacia():
            print("La lista está vacía")
        else:
             print(f"Último elemento: {self.__lista[self.__cant - 1]}")
    
    def anterior(self, pos):
        if self.vacia():
            print("La lista está vacía")
        elif pos <= 0 or pos > self.__cant:
            print("Posición inválida")
        else:
             print(f"Posición anterior: {pos - 1}")
    
    def siguiente(self, pos):
        if self.vacia():
            print("La lista está vacía")
        elif pos < 1 or pos >= self.__cant:
            print("Posición inválida")
        else:
             print(f"Posición siguiente: {pos + 1}")

    def recorrer(self):
        if self.vacia():
            print("La lista está vacía")
        else:
            print("Elementos de la lista:")
            for i in range(self.__cant):
                print(f"{self.__lista[i]}", end=" ")
            print("")
    
if __name__ == "__main__":
    lista_sec = listaSecuencial(4)
    lista_sec.insertar(7)
    lista_sec.insertar(4)
    lista_sec.insertar(2)
    lista_sec.insertar(6)
    lista_sec.recorrer()
    lista_sec.buscar(2)
    lista_sec.suprimir(1)
    lista_sec.recorrer()
    lista_sec.recuperar(2)
    lista_sec.buscar(3)
    lista_sec.buscar(4)
    lista_sec.primerElemento()
    lista_sec.ultimoElemento()
    lista_sec.siguiente(1)
    lista_sec.anterior(2)
