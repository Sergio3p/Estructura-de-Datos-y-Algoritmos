class Nodo:
    def __init__(self, dato):
        self.__dato = dato
        self.__sig = None

    def getDato(self):
        return self.__dato

    def getSig(self):
        return self.__sig

    def setSig(self, dato):
        self.__sig = dato

class ColaEnlazada:
    def __init__(self):
        self.__pr = None
        self.__ul = None
        self.__cant = 0

    def vacia(self):
        return self.__cant == 0

    def insertar(self, cliente):
        nuevo = Nodo(cliente)
        if self.vacia():
            self.__pr = nuevo
        else:
            self.__ul.setSig(nuevo)
        self.__ul = nuevo
        self.__cant += 1

    def suprimir(self):
        if self.vacia():
            print("La lista está vacía")
        else:
            dato = self.__pr.getDato()
            self.__pr = self.__pr.getSig()
            self.__cant -= 1
            if self.vacia():
                self.__ul = None
        return dato

    def getCant(self):
        return self.__cant

class Cliente:
    def __init__(self, llegada):
        self.__tiempo_llegada = llegada
        self.__tiempo_atendido = 0

    def getAtendido(self):
        return self.__tiempo_atendido

    def getLlegada(self):
        return self.__tiempo_llegada

class Cajero:
    def __init__(self, atencion):
        self.__tiempo_atencion = atencion
        self.__tiempo_restante = 0
        self._cola = ColaEnlazada()
        self.__clientes_atendidos = 0

    def atenderCliente(self, tiempo_actual):
        if self.__tiempo_restante == 0 and not self._cola.vacia():
            cliente = self._cola.suprimir()
            cliente._Cliente__tiempo_atendido = tiempo_actual
            self.__tiempo_restante = self.__tiempo_atencion
            self.__clientes_atendidos += 1
            return cliente  # Retornar el cliente atendido
        elif self.__tiempo_restante > 0:
            self.__tiempo_restante -= 1
        return None  # Si no hay cliente atendido

    def agregarCliente(self, cliente):
        self._cola.insertar(cliente)

    def getCantClientes(self):
        return self._cola.getCant()

    def getClientesAtendidos(self):
        return self.__clientes_atendidos

if __name__ == "__main__":
    tiempo_simulacion = 120
    tiempo_llegada_cliente = 2
    c1 = Cajero(5)
    c2 = Cajero(3)
    c3 = Cajero(4)
    cajeros = [c1, c2, c3]

    clientes_sin_atender = 0
    tiempos_espera = []

    for i in range(tiempo_simulacion):
        if i % tiempo_llegada_cliente == 0:
            nuevo_cliente = Cliente(i)
            colasCajeros = [cajero.getCantClientes() for cajero in cajeros]
            min_cola = min(colasCajeros)
            indice = 0
            encontrado = False
            while indice < len(colasCajeros) and not encontrado:
                if colasCajeros[indice] == min_cola:
                    cajeros[indice].agregarCliente(nuevo_cliente)
                    encontrado = True
                indice += 1

        for cajero in cajeros:
            cliente_atendido = cajero.atenderCliente(i)
            if cliente_atendido:
                tiempo_espera = i - cliente_atendido.getLlegada()
                tiempos_espera.append(tiempo_espera)

    # Contar los clientes sin atender
    for cajero in cajeros:
        clientes_sin_atender += cajero.getCantClientes()  # Contar los que quedaron en cola

    # Calcular métricas
    if tiempos_espera:
        max_espera = max(tiempos_espera)
    else:
        max_espera = 0

    # Calcular el promedio de espera
    if tiempos_espera:
        suma_esperas = sum(tiempos_espera)
        cantidad_atendidos = len(tiempos_espera)
        promedio_espera = suma_esperas / cantidad_atendidos
    else:
        promedio_espera = 0

    # Contar el total de clientes atendidos
    total_clientes_atendidos = 0
    for cajero in cajeros:
        total_clientes_atendidos += cajero.getClientesAtendidos()

    clientes_atendidos = total_clientes_atendidos

    print(f"""
        'clientes_atendidos': {clientes_atendidos},
        'clientes_sin_atender': {clientes_sin_atender},
        'max_espera': {max_espera},
        'promedio_espera_atendidos': {promedio_espera},
        'promedio_espera_sin_atencion': {clientes_sin_atender}
    """)
