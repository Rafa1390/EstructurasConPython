from Nodo import Nodo

class Cola:
    def __init__(self):
        self.long = 0
        self.frente = Nodo()
        self.final = Nodo()

    def es_vacia(self):
        vacia = False
        if self.frente is None or self.frente.valor is None:
            vacia = True
        return vacia

    def insertar_elemento(self, dato):
        nuevo = Nodo(dato)

        if self.es_vacia():
            self.frente = nuevo
            self.final = nuevo
        else:
            self.final.sig = nuevo
            self.final = nuevo

        self.long += 1

    def atender(self):
        num = Nodo()

        if not self.es_vacia():
            aux = self.frente
            num = aux
            self.frente = aux.sig
            aux.sig = None
            self.long -= 1

        return num
