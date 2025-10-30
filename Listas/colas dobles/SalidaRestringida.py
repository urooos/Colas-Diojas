import sys
sys.path.append("c:\\Users\\oitw4\\OneDrive\\Desktop\\Colas_Diojas\\Clases")
from clase_NodoPrev import Node

class OutputRestrictedDeque:
    def __init__(self):
        self.head = None
        self.rear = None
        
    def isEmpty(self):
        return self.head is None
    
    def push_front(self, data):
        new_node = Node(data)     
        if self.isEmpty(): #Si la cola esta vacia
            self.head = new_node #Head apunta al nuevo nodo
            self.rear = new_node #Rear apunta al nuevo nodo
        else:
            new_node.next = self.head #El siguiente del nuevo nodo es el nodo que apunta head
            self.head.prev = new_node #El prev del antiguo head apunta al nuevo nodo
            self.head = new_node #Head apunta al nuevo nodo
            
    def push_rear(self, data):
        new_node = Node(data) #Creamos un nuevo nodo
        if self.isEmpty(): #Si la cola esta vacia
            self.head = new_node #Head apunta al nuevo nodo
            self.rear = new_node #Rear apunta al nuevo nodo
        else:
            new_node.prev = self.rear #El prev del nuevo nodo apunta al nodo actual rear
            self.rear.next = new_node #El siguiente del nodo que apunta rear es el nuevo nodo
            self.rear = new_node #Rear apunta al nuevo nodo
            
    def pop_front(self):
        if self.isEmpty(): #Si la cola esta vacia
            raise Exception("La cola esta vacia") #Lanzamos un error si esta vacia
        data = self.head.data #Guardamos el dato del nodo que apunta head
        self.head = self.head.next #Hacemos que head apunte al siguiente nodo
        if self.head is None: #Si la cola queda vacia despues de hacer pop
            self.rear = None #Rear tambien apunta a None
        else:
            self.head.prev = None #El prev del nuevo head apunta a None
        return data #Regresamos el dato del nodo que se elimino
    
    def show(self):
        if self.isEmpty():
            print("La cola está vacía")
            return
        h = self.head
        while h is not None:
            print(f"{h.data} -> ", end="")
            h = h.next
        print("None")
        
print("Solo se puede eliminar por el frente y agregar por ambos extremos:")
myDeque = OutputRestrictedDeque() #Creamos una instancia de la clase OutputRestrictedDeque. Instancia = objeto
myDeque.push_front(1) #Agregamos elementos a la cola por el frente
myDeque.push_rear(2) #Agregamos elementos a la cola por la parte trasera
myDeque.show() #Mostramos la lista que representa la cola
print("Agregamos otro elemento por el frente")
myDeque.push_front(0) #Agregamos otro elemento al frente
myDeque.show() #Mostramos la lista que representa la cola
print("Agregamos otro elemento al final")
myDeque.push_rear(3) #Agregamos otro elemento al final
myDeque.show() #Mostramos la lista que representa la cola
print("Eliminamos el elemento al frente")
myDeque.pop_front() #Eliminamos un elemento del frente
myDeque.show() #Mostramos la lista después de eliminar
