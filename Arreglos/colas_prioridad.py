class PriorityQueue:
    def __init__(self, capacity):
        self.capacity = capacity #Capacidad maxima de la cola
        self.queue = [None] * capacity #Creamos una lista que se iniciliza con none en cada posicion segun la capacidad
        self.size = 0 #Tamaño actual de la cola
        
    def isEmpty(self):
        return self.size == 0 #Regresa True si la cola esta vacia
    
    def isFull(self):
        return self.size == self.capacity #Regresa True si la cola esta llena
    
    def enqueue(self, data, priority):
        if self.isFull(): #Si la cola esta llena
            raise Exception("La cola esta llena")
        
        new_element = (data, priority) #Creamos una tupla con el dato y su prioridad es una tupla porque cada elemento tiene dos valores y es tupla y no lista porque no se va a modificar
        
        if self.isEmpty(): #Si la cola esta vacia
            self.queue[0] = new_element #Agregamos el nuevo elemento en la primera posicion
        else:
            i = self.size - 1 #Indice del ultimo elemento en la cola
            while i >= 0 and self.queue[i][1] > priority: #Mientras i sea mayor o igual a 0 y la prioridad del elemento en la posicion i sea mayor que la prioridad del nuevo elemento
                self.queue[i + 1] = self.queue[i] #Movemos el elemento en la posicion i a la posicion i+1
                i -= 1 #Decrementamos i para seguir comparando con los elementos anteriores
            self.queue[i + 1] = new_element #Agregamos el nuevo elemento en la posicion correcta segun su prioridad
        self.size += 1 #Incrementamos el tamaño de la cola
        
    def dequeue(self):
        if self.isEmpty():
            raise Exception("La cola esta vacia")
        
        data = self.queue[0][0] #Guardamos el dato del primer elemento en la cola (FIFO)
        for i in range(1, self.size): #Movemos todos los elementos una posicion hacia adelante
            self.queue[i - 1] = self.queue[i]
        self.queue[self.size - 1] = None #Eliminamos el ultimo elemento que ahora es None
        self.size -= 1 #Decrementamos el tamaño de la cola
        return data #Regresamos el dato que se elimino
    
    def show(self):
        if self.isEmpty():
            print("La cola está vacía")
            return
        for i in range(self.size):
            print(f"({self.queue[i][0]}, prioridad: {self.queue[i][1]})", end=", ")
        print("")
        
myQueue = PriorityQueue(5) #Creamos una instancia de la clase PriorityQueue con capacidad 5
myQueue.enqueue("Tarea 1", 2) #Agregamos elementos a la cola con su prioridad
myQueue.enqueue("Tarea 2", 1)
myQueue.enqueue("Tarea 3", 3)
myQueue.show() #Mostramos la lista que representa la cola

print("Elemento desencolado por prioridad:", myQueue.dequeue())
myQueue.show() #Mostramos la lista que representa la cola
        
        