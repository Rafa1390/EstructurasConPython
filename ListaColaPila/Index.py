from Lista import Lista
from Cola import Cola
from Pila import Pila


def main():
    mi_lista = Lista()

    mi_lista.insertar_ordenado(5)
    mi_lista.insertar_ordenado(2)
    mi_lista.insertar_ordenado(8)

    mi_lista.mostrar_lista()

    # mi_lista.eliminar_elem(8)
    # mi_lista.eliminar_elem(2)
    # mi_lista.eliminar_elem(5)

    elim = mi_lista.eliminar_elem(5)
    print('')
    if elim == False:
        print('Lista vacia o dato incorrecto')

    mi_lista.mostrar_lista()

    # mi_cola = Cola()
    #
    # mi_cola.insertar_elemento(3)
    # mi_cola.insertar_elemento(2)
    # mi_cola.insertar_elemento(1)
    #
    # print(mi_cola.atender().get_valor())
    # print(mi_cola.atender().get_valor())
    # print(mi_cola.atender().get_valor())
    #
    # if mi_cola.atender().valor is None:
    #     print('Cola vacia')

    # mi_pila = Pila()
    #
    # mi_pila.push_elem(5)
    # mi_pila.push_elem(4)
    # mi_pila.push_elem(3)
    #
    # print(mi_pila.pop_elem().valor)
    # print(mi_pila.pop_elem().valor)
    # print(mi_pila.pop_elem().valor)
    #
    # if mi_pila.pop_elem().valor is None:
    #     print('Pila vacia')


if __name__ == "__main__":
    main()
