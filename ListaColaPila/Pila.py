from Nodo import Nodo

class Pila:
    def __init__(self):
        self.tope = Nodo()
        self.long = 0

    def es_vacia(self):
        vacia = False
        if self.tope is None or self.tope.valor is None:
            vacia = True
        return  vacia

    def push_elem(self, dato):
        nuevo = Nodo(dato)

        if self.es_vacia():
            self.tope = nuevo
        else:
            nuevo.sig = self.tope
            self.tope = nuevo

        self.long += 1

    def pop_elem(self):
        num = Nodo()

        if not self.es_vacia():
            aux = self.tope
            num = aux
            self.tope = aux.sig
            aux = None
            self.long -= 1

        return num