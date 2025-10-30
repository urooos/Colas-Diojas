import sys
sys.path.append("c:\\Users\\oitw4\\OneDrive\\Desktop\\Colas_Diojas\\Clases")
from clase_NodoPrev import Node

class InputRestrictedDeque:
    def __init__(self):
        self.head = None
        self.rear = None
        
    def isEmpty(self):
        return self.head is None 
    
    def push_back(self, data):
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

    def pop_rear(self):
        if self.isEmpty(): #Si la cola esta vacia
            raise Exception("La cola esta vacia") #Lanzamos un error si esta vacia
        data = self.rear.data #Guardamos el dato del ultimo nodo
        if self.head == self.rear: #Si solo hay un nodo en la cola
            self.head = None #Hacemos que head apunte a None, por lo que la cola queda vacia
            self.rear = None #Hacemos que rear apunte a None, por lo que la cola queda vacia
        else:
            self.rear = self.rear.prev #Rear apunta al penultimo nodo (usando prev)
            self.rear.next = None #Hacemos que el siguiente del nuevo rear apunte a None
        return data #Regresamos el dato del nodo que se elimino

    def show(self):
        if self.isEmpty():
            print("La cola está vacía")
            return
        h = self.head
        while h is not None:
            print(h.data, end=" -> ")
            h = h.next
        print("None")   
        
        
print("Solo se puede agregar por el final y eliminar por ambos extremos:")
myDeque = InputRestrictedDeque() #Creamos una instancia de la clase InputRestrictedDeque. Instancia = objeto
myDeque.push_back(1) 
myDeque.push_back(2)
myDeque.show() 
print("Agregamos otro elemento al final")
myDeque.push_back(3)
myDeque.show()
print("Elemento eliminado del frente:", myDeque.pop_front())
myDeque.show()
print("Elemento eliminado del final:", myDeque.pop_rear()) 
myDeque.show() 