import sys
sys.path.append("c:\\Users\\oitw4\\OneDrive\\Desktop\\Colas_Diojas\\Clases")
from clase_Nodo import Node

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

    def pop_rear(self):
        if self.isEmpty(): #Si la cola esta vacia
            raise Exception("La cola esta vacia") #Lanzamos un error si esta vacia
        if self.head == self.rear: #Si solo hay un nodo en la cola
            data = self.head.data #Guardamos el dato del unico nodo
            self.head = None #Hacemos que head apunte a None, por lo que la cola queda vacia
            self.rear = None #Hacemos que rear apunte a None, por lo que la cola queda vacia
            return data #Regresamos el dato del nodo que se elimino
        
        h = self.head
        while h.next != self.rear: #Mientras el siguiente del nodo que apunta h no sea rear   
            h = h.next #Movemos h al siguiente nodo
        data = self.rear.data #Guardamos el dato del ultimo nodo
        self.rear = h #Rear apunta al penultimo nodo
        self.rear.next = None #Hacemos que el siguiente del penultimo nodo apunte a None, por lo que el ultimo nodo se elimina de la cola
        return data #Regresamos el dato del nodo que se elimino
    
    def peek_front(self):
        if self.isEmpty(): 
            raise Exception("La cola esta vacia")
        
        return self.head.data #Regresamos el dato del nodo que apunta head sin eliminarlo
    
    def peek_rear(self):
        if self.isEmpty(): 
            raise Exception("La cola esta vacia")
        
        return self.rear.data #Regresamos el dato del nodo que apunta rear sin eliminarlo
    
    def mostrar(self):
        if self.isEmpty():
            print("La cola está vacía")
            return
        h = self.head
        while h is not None:
            print(h.data, end=" -> ")
            h = h.next
        print("None")   
        
myDeque = InputRestrictedDeque() #Creamos una instancia de la clase InputRestrictedDeque. Instancia = objeto
myDeque.push_back(1) #Agregamos elementos a la cola
myDeque.push_back(2)
myDeque.push_back(3)
myDeque.mostrar() #Mostramos la lista que representa la cola
print("Primer elemento:", myDeque.peek_front()) #Mostramos el primr elemento
print("Ultimo elemento:", myDeque.peek_rear()) #Mostramos el ultimo elemento
print("Elemento eliminado del frente:", myDeque.pop_front()) #Eliminamos el primer elemento
myDeque.mostrar() #Mostramos la lista que representa la cola
print("Elemento eliminado del final:", myDeque.pop_rear()) #Eliminamos el ultimo elemento
myDeque.mostrar() #Mostramos la lista que representa la cola
print("Primer elemento:", myDeque.peek_front()) #Mostramos el primr elemento
print("Ultimo elemento:", myDeque.peek_rear()) #Mostramos el ultimo elemento
