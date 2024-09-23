class Nodo:
    def __init__(self, coef, exp, sig=None):
        self.__coef = coef  # Coeficiente
        self.__exp = exp    # Exponente
        self.__sig = sig    # Puntero al siguiente nodo
    
    def get_coef(self):
        return self.__coef
    
    def get_exp(self):
        return self.__exp
    
    def get_sig(self):
        return self.__sig
    
    def set_sig(self, sig):
        self.__sig = sig


class ListaEncadenada:
    def __init__(self):
        self.__cabeza = None
    
    def vacia(self):
        return self.__cabeza is None
    
    def insertar(self, coef, exp):
        nuevo = Nodo(coef, exp)
        if self.vacia() or self.__cabeza.get_exp() < exp:
            nuevo.set_sig(self.__cabeza)
            self.__cabeza = nuevo
        else:
            aux = self.__cabeza
            while aux.get_sig() is not None and aux.get_sig().get_exp() >= exp:
                aux = aux.get_sig()
            nuevo.set_sig(aux.get_sig())
            aux.set_sig(nuevo)
    
    def recorrer(self):
        aux = self.__cabeza
        while aux is not None:
            print(f"{aux.get_coef()}x^{aux.get_exp()}", end=" ")
            if aux.get_sig() is not None:
                print("+", end=" ")
            aux = aux.get_sig()
        print()

    def sumar(self, otro):
        resultado = ListaEncadenada()
        aux1 = self.__cabeza
        aux2 = otro.__cabeza
        
        while aux1 is not None or aux2 is not None:
            if aux1 is None:
                resultado.insertar(aux2.get_coef(), aux2.get_exp())
                aux2 = aux2.get_sig()
            elif aux2 is None:
                resultado.insertar(aux1.get_coef(), aux1.get_exp())
                aux1 = aux1.get_sig()
            elif aux1.get_exp() == aux2.get_exp():
                coef_suma = aux1.get_coef() + aux2.get_coef()
                if coef_suma != 0:
                    resultado.insertar(coef_suma, aux1.get_exp())
                aux1 = aux1.get_sig()
                aux2 = aux2.get_sig()
            elif aux1.get_exp() > aux2.get_exp():
                resultado.insertar(aux1.get_coef(), aux1.get_exp())
                aux1 = aux1.get_sig()
            else:
                resultado.insertar(aux2.get_coef(), aux2.get_exp())
                aux2 = aux2.get_sig()
        return resultado

    def restar(self, otro):
        resultado = ListaEncadenada()
        aux1 = self.__cabeza
        aux2 = otro.__cabeza

        while aux1 is not None or aux2 is not None:
            if aux1 is None:
                resultado.insertar(-aux2.get_coef(), aux2.get_exp())
                aux2 = aux2.get_sig()
            elif aux2 is None:
                resultado.insertar(aux1.get_coef(), aux1.get_exp())
                aux1 = aux1.get_sig()
            elif aux1.get_exp() == aux2.get_exp():
                coef_resta = aux1.get_coef() - aux2.get_coef()
                if coef_resta != 0:
                    resultado.insertar(coef_resta, aux1.get_exp())
                aux1 = aux1.get_sig()
                aux2 = aux2.get_sig()
            elif aux1.get_exp() > aux2.get_exp():
                resultado.insertar(aux1.get_coef(), aux1.get_exp())
                aux1 = aux1.get_sig()
            else:
                resultado.insertar(-aux2.get_coef(), aux2.get_exp())
                aux2 = aux2.get_sig()
        return resultado

    def multiplicar_escalar(self, escalar):
        resultado = ListaEncadenada()
        aux = self.__cabeza

        while aux is not None:
            resultado.insertar(aux.get_coef() * escalar, aux.get_exp())
            aux = aux.get_sig()
        
        return resultado


if __name__ == "__main__":
    polinomio1 = ListaEncadenada()
    polinomio2 = ListaEncadenada()

    # Insertar términos en los polinomios (coeficiente, exponente)
    polinomio1.insertar(3, 2)
    polinomio1.insertar(5, 1)
    polinomio1.insertar(2, 0)

    polinomio2.insertar(1, 2)
    polinomio2.insertar(-5, 1)
    polinomio2.insertar(4, 0)

    print("Polinomio 1:")
    polinomio1.recorrer()

    print("Polinomio 2:")
    polinomio2.recorrer()

    # Sumar polinomios
    suma = polinomio1.sumar(polinomio2)
    print("Suma de polinomios:")
    suma.recorrer()

    # Restar polinomios
    resta = polinomio1.restar(polinomio2)
    print("Resta de polinomios:")
    resta.recorrer()

    # Multiplicación de un polinomio por un escalar
    escalar = 2
    producto = polinomio1.multiplicar_escalar(escalar)
    print(f"Polinomio 1 multiplicado por {escalar}:")
    producto.recorrer()
