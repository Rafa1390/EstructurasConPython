from Nodo import Nodo


class Lista:
    def __init__(self):
        self.cabeza = Nodo()
        self.long = 0

    def set_cabeza(self, x):
        self.cabeza = x

    def get_cabeza(self):
        return self.cabeza

    def get_long(self):
        return self.long

    def insertar_ordenado(self, dato):
        nuevo = Nodo(dato)

        if self.get_cabeza().get_valor() is None:
            self.set_cabeza(nuevo)

        elif nuevo.get_valor() < self.get_cabeza().get_valor():
            nuevo.set_sig(self.get_cabeza())
            self.set_cabeza(nuevo)

        else:
            ant = self.get_cabeza()
            act = self.cabeza.get_sig()

            # sig = self.cabeza.get_sig()
            # print(sig.valor)

            while act is not None and act.valor < nuevo.get_valor():
                ant = ant.get_sig()
                act = act.sig

            nuevo.set_sig(ant.get_sig())
            ant.set_sig(nuevo)

        self.long += 1

    def mostrar_lista(self):

        aux = self.get_cabeza()

        while aux is not None:
            print(aux.get_valor())
            aux = aux.get_sig()

    def eliminar_elem(self, dato):
        elim = False
        if self.cabeza is not None:
            aux = self.cabeza

            if self.cabeza.valor == dato:
                self.cabeza = self.cabeza.sig
                aux = None
            else:
                ant = self.cabeza
                act = self.cabeza.sig

                while act is not None and act.valor != dato:
                    ant = ant.sig
                    act = act.sig

                ant.sig = act.sig
                act = None

            self.long -= 1
            elim = True

        return elim