import sys
sys.path.append("c:\\Users\\oitw4\\OneDrive\\Desktop\\Colas_Diojas\\Clases")

from clase_Nodo import Node

class Deque:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head is None
    
    def enqueue_front(self, data):
        new_node = Node(data)     
        new_node.next = self.head #El siguiente del nuevo nodo es el nodo que apunta head #Si la cola esta vacia head es None por lo que new_node.next = None
        self.head = new_node #Head apunta al nuevo nodo
        
    def enqueue_rear(self, data):
        new_node = Node(data) #Creamos un nuevo nodo
        if self.isEmpty(): #Si la cola esta vacia
            self.head = new_node #Head apunta al nuevo nodo
        else:
            h = self.head
            while h.next is not None: #Mientras el siguiente del nodo que apunta h no sea null
                h = h.next #Movemos h al siguiente nodo
            h.next = new_node #Cuando h llega al ultimo nodo, el siguiente de este es el nuevo nodo
            
    def dequeue_front(self):
        if self.isEmpty(): #Si la cola esta vacia
            raise Exception("La cola esta vacia") #Lanzamos un error si esta vacia
        data = self.head.data #Guardamos el dato del nodo que apunta head
        self.head = self.head.next #Hacemos que head apunte al siguiente nodo
        return data #Regresamos el dato del nodo que se elimino 
    
    def dequeue_rear(self):
        if self.isEmpty(): #Si la cola esta vacia
            raise Exception("La cola esta vacia") #Lanzamos un error si esta vacia
        h = self.head
        if h.next is None: #Si solo hay un nodo en la cola
            data = h.data #Guardamos el dato del unico nodo
            self.head = None #Hacemos que head apunte a None, por lo que la cola queda vacia
            return data #Regresamos el dato del nodo que se elimino
        while h.next.next is not None: #Mientras el siguiente del siguiente del nodo que apunta h no sea null   
            h = h.next #Movemos h al siguiente nodo
        data = h.next.data #Guardamos el dato del ultimo nodo
        h.next = None #Hacemos que el siguiente del penultimo nodo apunte a None, por lo que el ultimo nodo se elimina de la cola
        return data #Regresamos el dato del nodo que se elimino
    