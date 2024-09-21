class PilaSecuencial: 
    lista: list
    tope: int           
    cant: int           

    def __init__(self): 
        self.tope = -1  
        self.cant = 8                   # Por ser un número binario de 8 bits.
        self.lista = [None] * self.cant 
        
    def vacia(self): 
        return self.tope == -1
        
    def insertar(self, elemento):
        cant = self.cant - 1
        if self.tope < cant:      
            self.tope += 1        
            self.lista[self.tope] = elemento  
        else:
            print("\nLa lista está llena.")

    def suprimir(self): 
        if self.vacia():
            print("\nLa pila está vacía")
        else:
            elemento = self.lista[self.tope]    
            self.tope -= 1                      
            print(f"\nSe suprimió el elemento {elemento}")
        
    def mostrar(self): 
        if self.vacia():
            print("\nLa pila está vacía.")
        else:
            print("\nPila: ", end='')       
            for i in range(self.tope, -1, -1):  
                print(self.lista[i], end=' ')
            print("\n")

    def convertirBinario(self,num:int):
        while num > 0:
            resto = num % 2
            self.insertar(resto)
            num = num // 2

if __name__ == '__main__':
    elemento = PilaSecuencial()
    elemento.convertirBinario(50)
    elemento.mostrar()
    