from Lista import Lista

class Estructuras:
    mi_lista = Lista()

    def agregar_lista(self, dato):
        self.mi_lista.insertar_ordenado(dato)

    def eliminar_lista(self, dato):
        self.mi_lista.eliminar_elem(dato)
