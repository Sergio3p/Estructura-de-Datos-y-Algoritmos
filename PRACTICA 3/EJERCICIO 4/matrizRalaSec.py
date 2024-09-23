import numpy as np

class listaSecuencial:
    def __init__(self, fila, columna):
        self.__lista = np.zeros((fila, columna), dtype=int)  # Crear la matriz
        self.__fila = fila
        self.__columna = columna
        self.__cant = 0  # Inicialmente la cantidad de elementos es 0
    
    def vacia(self):
        return self.__cant == 0

    def insertar(self, fila, columna, valor):
        if fila < self.__fila and columna < self.__columna:
            self.__lista[fila][columna] = valor
            self.__cant += 1
        else:
            print("Posición inválida")

    def recuperar(self, fila, columna):
        if fila < self.__fila and columna < self.__columna:
            return self.__lista[fila][columna]
        else:
            print("Posición inválida")
            return None
    
    def recorrer(self):
        for i in range(self.__fila):
            for j in range(self.__columna):
                print(self.__lista[i][j], end=" ")
            print("")

# Suma de matrices secuenciales
def sumar_matrices_secuenciales(matriz1, matriz2):
    resultado = np.zeros((matriz1._listaSecuencial__fila, matriz1._listaSecuencial__columna), dtype=int)
    for i in range(matriz1._listaSecuencial__fila):
        for j in range(matriz1._listaSecuencial__columna):
            resultado[i][j] = matriz1.recuperar(i, j) + matriz2.recuperar(i, j)
    return resultado

if __name__ == "__main__":
    f = 100
    c = 100
    
    matriz1 = listaSecuencial(f, c)
    matriz2 = listaSecuencial(f, c)
    
    # Asignar valores a las matrices usando el método insertar
    matriz1.insertar(0, 0, 5)
    matriz2.insertar(0, 0, 3)
    matriz1.insertar(1, 1, 7)
    matriz2.insertar(1, 1, 4)
    
    # Sumar matrices
    resultado = sumar_matrices_secuenciales(matriz1, matriz2)
    
    # Imprimir el resultado
    print("Resultado de la suma:")
    for fila in resultado:
        print(fila)
