import sys
sys.path.append("c:\\Users\\oitw4\\OneDrive\\Desktop\\Colas_Diojas\\Clases")
from clase_Nodo import Node

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
            self.head = new_node #Head apunta al nuevo nodo
            
    def push_rear(self, data):
        new_node = Node(data) #Creamos un nuevo nodo
        if self.isEmpty(): #Si la cola esta vacia
            self.head = new_node #Head apunta al nuevo nodo
            self.rear = new_node #Rear apunta al nuevo nodo
        else:
            self.rear.next = new_node #El siguiente del nodo que apunta rear es el nuevo nodo
            self.rear = new_node #Rear apunta al nuevo nodo
            
    def pop_front(self):
        if self.isEmpty(): #Si la cola esta vacia
            raise Exception("La cola esta vacia") #Lanzamos un error si esta vacia
        data = self.head.data #Guardamos el dato del nodo que apunta head
        self.head = self.head.next #Hacemos que head apunte al siguiente nodo
        if self.head is None: #Si la cola queda vacia despues de hacer pop
            self.rear = None #Rear tambien apunta a None
        return data #Regresamos el dato del nodo que se elimino
    
    def peek_front(self):
        if self.isEmpty(): 
            raise Exception("La cola esta vacia")
        
        return self.head.data #Regresamos el dato del nodo que apunta head sin eliminarlo
    
    def mostrar(self):
        if self.isEmpty():
            print("La cola está vacía")
            return
        h = self.head
        while h is not None:
            print(f"{h.data} -> ", end="")
            h = h.next
        print("None")
        
myDeque = OutputRestrictedDeque() #Creamos una instancia de la clase OutputRestrictedDeque. Instancia = objeto
myDeque.push_front(1) #Agregamos elementos a la cola por el frente
myDeque.push_rear(2) #Agregamos elementos a la cola por la parte trasera
myDeque.mostrar() #Mostramos la lista que representa la cola
myDeque.push_front(0) #Agregamos otro elemento al frente
print("Elemento agregado al frente: ", myDeque.peek_front())
myDeque.mostrar() #Mostramos la lista que representa la cola
myDeque.push_rear(3) #Agregamos otro elemento al final
print("Elemento agregado al final: ", myDeque.rear.data)
myDeque.mostrar() #Mostramos la lista que representa la cola
myDeque.pop_front() #Eliminamos un elemento del frente
