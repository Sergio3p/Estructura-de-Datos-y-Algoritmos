"""
Ejercicio Nº 6: 
El Laboratorio de Computación tiene una única impresora, a la cual llegan trabajos para imprimir 
de cualquiera de las máquinas. Considerando que los trabajos llegan cada 5 minutos a la cola de 
impresión.  Se  requiere  simular  el  comportamiento  de  dicha  cola, teniendo en cuenta  que cada trabajo tiene asociado el tiempo que se demorará el mismo en ser impreso; y que la impresora tiene un tiempo máximo para procesar cada trabajo de 5 minutos. Tener en cuenta que el trabajo que no se terminó de imprimir porque excedía su tiempo de proceso ingresa nuevamente a la cola con el tiempo restante de impresión. Suponga el tiempo de simulación de 1 hora.  
Se pide:  
a) Informar cantidad de trabajos que quedaron sin atender. 
b) Indicar el promedio de espera de los trabajos impresos. 
"""
import random
class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__sig = None

    def get_dato(self):
        return self.__dato
    
    def get_sig(self):
        return self.__sig
    
    def set_sig(self, dato):
        self.__sig = dato
    
class colaEncadenada:
    __cabeza:Nodo
    def __init__(self):
        self.__pr = None
        self.__ul = None
        self.__cant = 0
    
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self, dato):
        nuevo = Nodo(dato)
        if self.vacia():
            self.__pr = nuevo
        else:
            self.__ul.set_sig(nuevo)
        self.__ul = nuevo
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            print("La cola está vacía")
        else:
            dato = self.__pr.get_dato()
            self.__pr = self.__pr.get_sig()
            self.__cant -= 1
            if self.vacia():
                self.__ul = None
            return dato
        
    def recorrer(self):
        if self.vacia():
            print("La cola está vacía")
            return
        else:
            actual = self.__pr
            while actual is not None:
                print(actual.get_dato(), end=" ")
                actual = actual.get_sig()
    
    def impresion(self):
        tiempo_simulacion = 60  # tiempo de simulación en minutos
        tiempo_actual = 0
        trabajos_impresos = 0
        trabajos_reingresados = 0
        total_espera = 0

        while tiempo_actual < tiempo_simulacion:
            # Inserción de trabajo cada 5 minutos (trabajo, tiempo_llegada)
            trabajo = random.randint(1, 10)
            self.insertar((trabajo, tiempo_actual))

            if not self.vacia():
                tiempo_trabajo, tiempo_llegada = self.suprimir()

                # Tiempo de espera es el tiempo actual menos el tiempo de llegada del trabajo
                tiempo_espera = tiempo_actual - tiempo_llegada

                if tiempo_trabajo <= 5:
                    trabajos_impresos += 1
                    total_espera += tiempo_espera
                else:
                    # Reinserta con el tiempo restante y actualiza el tiempo de llegada
                    tiempo_restante = tiempo_trabajo - 5
                    self.insertar((tiempo_restante, tiempo_actual))
                    trabajos_reingresados += 1

            tiempo_actual += 5  # Incrementa el tiempo de simulación cada 5 minutos

        print(f"La cantidad de trabajos sin atender es de: {trabajos_reingresados}")
        if trabajos_impresos > 0:
            promedio_espera = total_espera // trabajos_impresos
            print(f"El promedio de espera de los trabajos impresos es de: {promedio_espera} minutos")
        else:
            print("No hay trabajos impresos")
            
if __name__ == "__main__":
    impresora = colaEncadenada()
    impresora.impresion()