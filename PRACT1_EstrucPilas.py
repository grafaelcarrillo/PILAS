class Pila:
    def __init__(self):
        self.pila = []
        self.tam_max = 8

    def esta_vacia(self):
        return len(self.pila) == 0

    def esta_llena(self):
        return len(self.pila) == self.tam_max

    def apilar(self, elemento):
        if not self.esta_llena():
            self.pila.append(elemento)
        else:
            print("La pila está llena. No se puede apilar más elementos.")

    def desapilar(self):
        if not self.esta_vacia():
            return self.pila.pop()
        else:
            return "La pila está vacía"

    def tamano(self):
        return len(self.pila)
    
    def imprimir_pila(self):
        if not self.esta_vacia():
            print("Contenido de la pila:")
            for elemento in self.pila:
                print(elemento)
        else:
            print("La pila está vacía")

pila = Pila()

pila.apilar("x")
pila.apilar("y")
pila.desapilar()
pila.desapilar()
pila.desapilar()
pila.apilar("v")
pila.apilar("w")
pila.desapilar()
pila.apilar("r")
print("La pila tiene", pila.tamano(), "elementos.")
pila.imprimir_pila()