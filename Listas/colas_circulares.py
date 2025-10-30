import sys
sys.path.append("c:\\Users\\oitw4\\OneDrive\\Desktop\\Colas_Diojas\\Clases")

from clase_Nodo import Node 

class CircularQueue:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head is None
    
    def enqueue(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
            new_node.next = new_node  # Apunta a sí mismo para formar un círculo
        else:
            h = self.head
            while h.next != self.head: #Mientras h.next no apuntea a head
                h = h.next #H avanza al siguiente nodo, hasta llegar al ultimo nodo donde h.next apunta a head
            h.next = new_node #El siguiente del ultimo nodo ahora es el nuevo nodo
            new_node.next = self.head #En nuevo nodo apunta a head para mantener la circularidad
            
    def dequeue(self):
        if self.isEmpty():
            raise Exception("La cola está vacía")
        
        data = self.head.data
        if self.head.next == self.head:  # Si hay solo un nodo en la cola
            self.head = None #Se borra el unico nodo
        else:
            h = self.head
            while h.next != self.head: #Mientras h.next no apunte a head
                h = h.next #H avanza al siguiente nodo, hasta llegar al ultimo nodo donde h.next apunta a head
            h.next = self.head.next #El siguiente del ultimo nodo ahora es el segundo nodo 
            self.head = self.head.next #Actualizamos head al segundo nodo por lo que el primero se elimina de la cola y se mantiene la circularidad
        return data
    
    def show(self):
        if self.isEmpty():
            print("La cola está vacía")
            return
        h = self.head
        while True:
            print(h.data, end=" -> ")
            h = h.next
            if h == self.head:
                break
        print("Vuelve al inicio")
        
myQueue = CircularQueue()
myQueue.enqueue(1)  
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.show() #Mostramos la lista que representa la cola

print("Elemento desencolado:", myQueue.dequeue())
myQueue.show() #Mostramos la lista que representa la cola