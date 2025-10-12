#colas con listas enlazadas sin los apuntadores front y rear
import sys
sys.path.append("c:\\Users\\oitw4\\OneDrive\\Desktop\\Colas_Diojas\\Clases")
from clase_Nodo import Node
        
class Queue:
    def __init__(self):
        self.head = None #Head no apunta a ningun nodo
        
    def isEmpty(self):
        return self.head is None #Regresa True si la cola esta vacia
    
    def enqueue(self, data):
        new_node = Node(data) #Creamos un nuevo nodo
        
        if not self.head is None: #Si la cola no esta vacia
            h = self.head #Creamos el apuntador auxiliar h que apunta donde head
            while h.next is not None: #Mientras el siguiente del nodo que apunta h no sea null
                h = h.next #Movemos h al siguiente nodo
            h.next = new_node #Cuando h llega al ultimo nodo, el siguiente de este es el nuevo nodo
        else: self.head = new_node #Si la cola esta vacia, head apunta al nuevo nodo
    
    def dequeue(self):
        if self.isEmpty(): #Si la cola esta vacia
            raise Exception("La cola esta vacia") #Lanzamos un error si esta vacia
        data = self.head.data #Guardamos el dato del nodo que apunta head
        self.head = self.head.next #Hacemos que head apunte al siguiente nodo
        return data #Regresamos el dato del nodo que se elimino
    
    def peek(self):
        if self.isEmpty(): 
            print("La cola esta vacia")
        
        return self.head.data #Regresamos el dato del nodo que apunta head sin eliminarlo
        
myQueue = Queue() #Creamos una instancia de la clase Queue. Instancia = objeto

myQueue.enqueue(1) #Agregamos elementos a la cola
myQueue.enqueue(2)
myQueue.enqueue(3)

print("Primer elemento:", myQueue.peek()) #Mostramos el primr elemento
print("Elemento eliminado:", myQueue.dequeue()) #Eliminamos el primer elemento
print("Nuevo primer elemento:", myQueue.peek()) #Mostramos el nuevo primer elemento

