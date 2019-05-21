from Lista import Lista
from Pila import Pila
from Cola import Cola

class Estructuras:
    mi_lista = Lista()
    mi_pila = Pila()
    mi_cola = Cola()

    def ingresar_lista(self, dato):
        self.mi_lista.insertar_ordenado(dato)

    def eliminar_de_lista(self, dato):
        self.mi_lista.eliminar_elem(dato)

    def mostrar_lista(self):
        self.mi_lista.mostrar_lista()

    def ingresar_pila(self,dato):
        self.mi_pila.push_elem(dato)

    def eliminar_pila(self):
        self.mi_pila.pop_elem()

    def ingresar_cola(self,dato):
        self.mi_cola.insertar_elemento(dato)

    def eliminar_cola(self):
        self.mi_cola.atender()