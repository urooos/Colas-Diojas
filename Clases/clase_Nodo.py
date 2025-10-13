class Node:
    def __init__(self, data, prioridad=None):
        self.data = data #Dato del nodo
        self.prioridad = prioridad #Prioridad del nodo, por defecto es None
        self.next = None #Apunta al siguiente nodo
        