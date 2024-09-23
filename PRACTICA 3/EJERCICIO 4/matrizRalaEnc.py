class Nodo:
    def __init__(self, fila, columna, valor, sig=None):
        self.__fila = fila
        self.__columna = columna
        self.__valor = valor
        self.__sig = sig
    
    def get_fila(self):
        return self.__fila
    
    def get_columna(self):
        return self.__columna
    
    def get_valor(self):
        return self.__valor
    
    def get_sig(self):
        return self.__sig
    
    def set_sig(self, sig):
        self.__sig = sig


class ListaEncadenada:
    def __init__(self):
        self.__cabeza = None
        self.__cant = 0
    
    def getCabeza(self):
        return self.__cabeza
    
    def vacia(self):
        return self.__cabeza is None
    
    def insertar(self, fila, columna, valor):
        if valor != 0:  # Solo insertamos valores no nulos
            nuevo = Nodo(fila, columna, valor)
            if self.vacia():
                self.__cabeza = nuevo
            else:
                aux = self.__cabeza
                while aux.get_sig() is not None:
                    aux = aux.get_sig()
                aux.set_sig(nuevo)
            self.__cant += 1
    
    def recorrer(self):
        if self.vacia():
            print("La matriz está vacía.")
        else:
            aux = self.__cabeza
            while aux is not None:
                print(f"Fila: {aux.get_fila()}, Columna: {aux.get_columna()}, Valor: {aux.get_valor()}")
                aux = aux.get_sig()

    def recuperar(self, fila, columna):
        if self.vacia():
            print("La matriz está vacía.")
        else:
            aux = self.__cabeza
            while aux is not None:
                if aux.get_fila() == fila and aux.get_columna() == columna:
                    return aux.get_valor()
                aux = aux.get_sig()
        return 0  # Si no se encuentra el valor, se considera un 0 (para una matriz rala)

    def eliminar(self, fila, columna):
        if self.vacia():
            print("La matriz está vacía.")
        else:
            if self.__cabeza.get_fila() == fila and self.__cabeza.get_columna() == columna:
                self.__cabeza = self.__cabeza.get_sig()
                self.__cant -= 1
                return
            aux = self.__cabeza
            while aux.get_sig() is not None:
                if aux.get_sig().get_fila() == fila and aux.get_sig().get_columna() == columna:
                    aux.set_sig(aux.get_sig().get_sig())
                    self.__cant -= 1
                    return
            print(f"No se encontró un valor en ({fila}, {columna})")


def sumar_matrices_ralas(matriz1, matriz2):
    resultado = ListaEncadenada()
    
    # Recorremos la primera matriz y sumamos sus elementos con los de la segunda matriz
    aux1 = matriz1.getCabeza()
    while aux1 is not None:
        fila = aux1.get_fila()
        columna = aux1.get_columna()
        valor1 = aux1.get_valor()
        valor2 = matriz2.recuperar(fila, columna)
        suma = valor1 + valor2
        resultado.insertar(fila, columna, suma)
        aux1 = aux1.get_sig()
    
    # Recorremos la segunda matriz para agregar los elementos que no están en la primera matriz
    aux2 = matriz2.getCabeza()
    while aux2 is not None:
        fila = aux2.get_fila()
        columna = aux2.get_columna()
        if matriz1.recuperar(fila, columna) == 0:  # Si la posición no está en la primera matriz
            resultado.insertar(fila, columna, aux2.get_valor())
        aux2 = aux2.get_sig()
    
    return resultado


if __name__ == "__main__":
    matriz1 = ListaEncadenada()
    matriz1.insertar(0, 0, 1)
    matriz1.insertar(1, 2, 5)
    matriz1.insertar(3, 3, 8)

    matriz2 = ListaEncadenada()
    matriz2.insertar(0, 0, 2)
    matriz2.insertar(1, 2, 3)
    matriz2.insertar(2, 2, 4)

    print("Matriz 1:")
    matriz1.recorrer()

    print("Matriz 2:")
    matriz2.recorrer()

    print("Suma de matrices:")
    matriz_suma = sumar_matrices_ralas(matriz1, matriz2)
    matriz_suma.recorrer()
