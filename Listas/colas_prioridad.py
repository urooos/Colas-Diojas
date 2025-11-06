import sys
sys.path.append("c:\\Users\\oitw4\\OneDrive\\Desktop\\Colas_Diojas\\Clases")
from clase_Nodo import Node

class PriorityQueue:
    def __init__(self):
        self.head = None #Head no apunta a ningun nodo
        
    def isEmpty(self):
        return self.head is None #Regresa True si la cola esta vacia
    
    def enqueue(self, data, prioridad):
        new_node = Node(data, prioridad) #Creamos un nuevo nodo con data y prioridad
        
        if self.isEmpty() or self.head.prioridad > prioridad: #Si la cola esta vacia o la prioridad del nuevo nodo es mayor que la del nodo que apunta head
            new_node.next = self.head #El siguiente del nuevo nodo es el nodo que apunta head #Si la cola esta vacia head es None por lo que new_node.next = None
            self.head = new_node #Head apunta al nuevo nodo
            return
        h = self.head #Creamos el apuntador auxiliar h que apunta donde head
        while h.next is not None and h.next.prioridad <= prioridad: #Mientras el siguiente del nodo que apunta h no sea null y la prioridad del siguiente nodo sea menor o igual a la prioridad del nuevo nodo
            h = h.next #Movemos h al siguiente nodo
        new_node.next = h.next #El siguiente del nuevo nodo es el siguiente del nodo que apunta h
        h.next = new_node #El siguiente del nodo que apunta h es el nuevo nodo
        
    def dequeue(self):
        if self.isEmpty(): #Si la cola esta vacia
            raise Exception("La cola esta vacia") #Lanzamos un error si esta vacia
        data = self.head.data #Guardamos el dato del nodo que apunta head
        self.head = self.head.next #Hacemos que head apunte al siguiente nodo
        return data #Regresamos el dato del nodo que se elimino
    
    def show(self):
        if self.isEmpty():
            print("La cola está vacía")
            return
        h = self.head
        while h is not None:
            print(f"({h.data}, prioridad: {h.prioridad})", end=" -> ")
            h = h.next
        print("None")
        
myQueue = PriorityQueue() #Creamos una instancia de la clase PriorityQueue. Instancia = objeto
myQueue.enqueue("Tarea 1", 2) #Agregamos elementos a la cola con su prioridad
myQueue.enqueue("Tarea 2", 1)
myQueue.enqueue("Tarea 3", 3)
myQueue.enqueue("Tarea 4", 1)
myQueue.show() #Mostramos la lista que representa la cola

print("Elemento desencolado por prioridad:", myQueue.dequeue())
myQueue.show() #Mostramos la lista que representa la cola
