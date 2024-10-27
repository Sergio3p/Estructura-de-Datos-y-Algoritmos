import numpy as np
import sys

class Grafo:
    def __init__(self):
        self.__tamaño = 0
        self.__vertices = []
        self.__matriz = np.zeros((self.__tamaño, self.__tamaño), dtype=int)
        self.__aristas = 0

    def agregar_vertice(self, vertice):
        if vertice in self.__vertices:
            print("El vértice ya existe.")
            return
        self.__tamaño += 1
        self.__matriz = np.resize(self.__matriz, (self.__tamaño, self.__tamaño))
        self.__vertices.append(vertice)

    def agregar_arista(self, v1, v2, peso):
        if v1 not in self.__vertices or v2 not in self.__vertices:
            print("Error: Uno o ambos vértices no existen.")
            return
        
        if peso != 0:
            idx1 = self.__vertices.index(v1)
            idx2 = self.__vertices.index(v2)
            self.__matriz[idx1][idx2] = peso
            self.__aristas += 1
        else:
            print("Error: El peso de la arista no puede ser cero.")

    def obtener_vertices(self):
        print(self.__vertices)
    
    def mostrar_matriz_adyacencia(self):
        print(" ", " ".join(self.__vertices))
        for i in range(len(self.__vertices)):
            print(self.__vertices[i], " ".join(map(str, self.__matriz[i])))

    def dijkstra(self, inicio):
        num_vertices = len(self.__vertices)
        distancias = [sys.maxsize] * num_vertices
        conocidos = [False] * num_vertices
        camino = [None] * num_vertices

        # Establecer la distancia inicial a 0
        distancias[self.__vertices.index(inicio)] = 0

        print(f"Inicio del algoritmo Dijkstra desde el vértice: {inicio}")
        print("Estado inicial:")
        print(f"Distancias: {distancias}")
        print(f"Conocidos: {conocidos}")
        print(f"Camino: {camino}")

        for _ in range(num_vertices):
            # Seleccionar el vértice con la distancia más corta y desconocido
            min_dist = sys.maxsize
            v = -1
            for i in range(num_vertices):
                if not conocidos[i] and distancias[i] < min_dist:
                    min_dist = distancias[i]
                    v = i

            if v == -1:  # Si no se encontró un vértice válido
                break

            # Marcar el vértice como conocido
            conocidos[v] = True
            print(f"\nVértice seleccionado: {self.__vertices[v]} con distancia {min_dist}")
            print("Estado después de marcarlo como conocido:")
            print(f"Distancias: {distancias}")
            print(f"Conocidos: {conocidos}")

            # Actualizar distancias de los vértices adyacentes
            for w in range(num_vertices):
                if self.__matriz[v][w] > 0 and not conocidos[w]:  # Si hay arista y w es desconocido
                    nueva_distancia = distancias[v] + self.__matriz[v][w]
                    if nueva_distancia < distancias[w]:
                        distancias[w] = nueva_distancia
                        camino[w] = v  # Guardar el índice del vértice anterior
                        print(f"  Actualizando distancia para {self.__vertices[w]}: {nueva_distancia} (previo: {distancias[w]})")
                        
            print(f"Estado después de actualizar las distancias:")
            print(f"Distancias: {distancias}")
            print(f"Conocidos: {conocidos}")
            print(f"Camino: {camino}")

        # Imprimir el resultado final
        print("\nDistancias finales desde el vértice", inicio)
        for i in range(num_vertices):
            print(f"{inicio} -> {self.__vertices[i]}: {distancias[i]}, Camino: {self.__get_camino(camino, inicio, self.__vertices[i])}")

    def __get_camino(self, camino, inicio, fin):
        ruta = []
        actual = self.__vertices.index(fin)
        while actual is not None:
            ruta.append(self.__vertices[actual])
            actual = camino[actual]  # Usa el índice guardado
        ruta.reverse()
        return " -> ".join(ruta)

def menu():
    op = int(input("""    
            Menú del Grafo:
        1. Agregar un vértice
        2. Agregar una arista
        3. Mostrar vertices           
        4. Mostrar matriz de adyacencia
        5. Algoritmo de Dijkstra
        0. Salir
    """))
    return op

if __name__ == "__main__":
    g = Grafo()
    opcion = menu()
    while opcion != 0:
        if opcion == 1:
            v = input("Ingrese el vértice: ")
            g.agregar_vertice(v)
        elif opcion == 2:
            v1 = input("Ingrese el primer vértice: ")
            v2 = input("Ingrese el segundo vértice: ")
            peso = int(input("Ingrese el peso de la arista: "))
            g.agregar_arista(v1, v2, peso)
        elif opcion == 3:
            g.obtener_vertices()
        elif opcion == 4:
            g.mostrar_matriz_adyacencia()
        elif opcion == 5:
            inicio = input("Ingrese el vértice de inicio: ")
            g.dijkstra(inicio)
        else:
            print("Opción inválida")
        opcion = menu()

"""
1
A
1
B
1
C
1
D
1
E
1
F
2
A
B
3
2
A
D
6
2
B
C
1
2
C
D
2
2
D
B
3
2
B
F
1
2
B
E
2
2
F
D
1
2
F
A
5
2
E
F
2
2
E
D
3

"""