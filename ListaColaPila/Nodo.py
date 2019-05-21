class Nodo:
    #def __init__(self):
    #    self.valor = 0
    #    self.sig = None

    def __init__(self, x=None):
        self.valor = x
        self.sig = None

    def set_valor(self, x):
        self.valor = x

    def get_valor(self):
        return self.valor

    def set_sig(self, x):
        self.sig = x

    def get_sig(self):
        return self.sig
