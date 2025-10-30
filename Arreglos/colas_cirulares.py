class CircularQueue: 
    def __init__(self, capacity):
        self.capacity = capacity #Capacidad maxima de la cola
        self.queue = [None] * capacity #Creamos una lista que se iniciliza con none en cada posicion segun la capacidad
        self.front = -1 #-1 indica que la cola esta vacia
        self.rear = -1 #Rear es el indice del ultimo elemento en la cola
        
    def isEmpty(self):
        return self.front == -1 #Regresa True si la cola esta vacia
    
    def isFull(self):
        return (self.rear +1) % self.capacity == self.front #Regresa True si la cola esta llena, osease si el resultado de la operacion es igual a front. Ejemplo: front = 0, rear = 4, capacity = 5. (4+1)%5 = 0 == front -> cola llena
    
    def enqueue(self, data):
        if self.isFull(): #Si la cola esta llena
            raise Exception("La cola esta llena") 
        
        if self.isEmpty(): #Si la cola esta vacia
            self.front = 0 #Hacemos que front apunte al primer indice
        self.rear = (self.rear + 1) % self.capacity #Movemos rear al siguiente indice de forma circular. Ejemplo rear = 3, capacity = 5. (3+1)%5 = 4 -> rear = 4. Se inserta en la posicion 4. Si rear = 4, (4+1)%5 = 0 -> rear = 0. Se inserta en la posicion 0
        
        self.queue[self.rear] = data #Agregamos el dato en la posicion de rear porque rear es el indice del ultimo elemento en la cola
        
    def dequeue(self):
        if self.isEmpty(): 
            raise Exception("La cola esta vacia") 
        
        dato = self.queue[self.front] #Guardamos el dato que apunta front pues es el primer elemento en la cola (FIFO)
        if self.front == self.rear: #Si solo hay un elemento en la cola
            self.front = -1 #Hacemos que front y rear apunten a -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity #Movemos front al siguiente indice de forma circular
        
        return dato #Regresamos el dato que se elimino

    def show(self):
        if self.isEmpty():
            print("La cola está vacía")
            return

        i = self.front #Apuntador auxiliar que inicia en front
        while True:
            print(self.queue[i], end=", ")
            if i == self.rear: #Rompe el ciclo cuando i llegue a rear, osease al ultimo elemento en la cola
                break
            i = (i + 1) % self.capacity #Movemos i al siguiente indice de forma circular
        print("")
        
    
myQueue = CircularQueue(5) #Creamos una instancia de la clase CircularQueue con capacidad 4

myQueue.enqueue(1) #Agregamos elementos a la cola
myQueue.enqueue(2)  
myQueue.enqueue(3)
myQueue.show() #Mostramos la lista que representa la cola
print("Elemento eliminado:", myQueue.dequeue()) #Eliminamos el primer elemento

myQueue.show() 
print("Agregamos tres elementos para demostrar circularidad...")
myQueue.enqueue(4)
myQueue.enqueue(5) 
myQueue.enqueue(6) 
myQueue.show()
