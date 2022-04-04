class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izq = None
        self.der = None

def buscar(raizDeUnArbol : Nodo, loQueEstaBuscando : int):
    if raizDeUnArbol == None:
        return False
    if raizDeUnArbol.dato == loQueEstaBuscando:
        return True
    else:
        estaPorLaIzquierda = buscar(raizDeUnArbol.izq, loQueEstaBuscando)
        estaPorLaDerecha = buscar(raizDeUnArbol.der, loQueEstaBuscando)
        if estaPorLaIzquierda == True:
            return True
        if estaPorLaDerecha == True:
            return True
        return False
