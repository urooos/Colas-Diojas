class Queue:
    def __init__(self):
        self.queue = []  #creamos una variable llamada queue para guardar los elementos en una lista. usamos self para poder acceder a ella desde otros metodos de la clase

    def is_empty(self):
        return not self.queue #Una lista vacia es False, una con elementos es True, usamos not para que concuerde con en el nombre del metodo

    def enqueue(self, element):
        self.queue.append(element) #Agregamos un elemento al final de la cola

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) #Eliminamos el primer elemento de la cola si la cola no esta vacia
        else: 
            raise IndexError("La cola esta vacia, no se puede eliminar un elemento") #indexError indicia que se intnento acceder a un indice que no existe en la lista 

    def peek(self):   
        if not self.is_empty():
            return self.queue[0] #Mostramos el primer elemento de la cola sin eliminarlo
        else:
            raise IndexError("La cola esta vacia, no se puede eliminar un elemento")



myQueue = Queue() #creamos una insancia de la clase Queue
#una instancia es un objeto creado a partir de la clase, con sus propios atributos y metodos 

myQueue.enqueue(1) #Agregamos elelementos a la cola
myQueue.enqueue(2)
myQueue.enqueue(3)
primer_dato = myQueue.peek() #Mostramos el primer elemento de la cola sin eliminarlo
print(primer_dato) #Imprimimos el primer elemento de la cola

myQueue.dequeue() #Eliminamos el primer elemento de la cola 
primer_dato = myQueue.peek() #Mostramos el primer elemento de la cola sin eliminarlo
print(primer_dato) #Imprimimos el primer elemento de la cola

print(myQueue.queue) #Impimimos la variable queue de la instancia myQueue
