class Deque:
    def __init__(self, capacity):
        self.capacity = capacity #Capacidad maxima del deque
        self.deque = [None] * capacity #Creamos una lista que se iniciliza con none en cada posicion segun la capacidad
        self.front = -1 #-1 indica que el deque esta vacio
        self.rear = -1 #Rear es el indice del ultimo elemento en el deque
        
    def isEmpty(self):
        return self.front == -1 #Regresa True si el deque esta vacio
    
    def isFull(self):
        return (self.rear +1) % self.capacity == self.front #Regresa True si el deque esta lleno, osease si el resultado de la operacion es igual a front. Ejemplo: front = 0, rear = 4, capacity = 5. (4+1)%5 = 0 == front -> deque lleno
    
    def addFront(self, data): #Agrega un elemento al frente del deque
        if self.isFull(): #Si el deque esta lleno
            raise Exception("El deque esta lleno, no se puede agregar un elemento al frente") 

        if self.isEmpty(): #Si el deque esta vacio
            self.front = 0 #Hacemos que front apunte al primer indice
            self.rear = 0 #Hacemos que rear apunte al primer indice
        else:
            self.front = (self.front - 1 + self.capacity) % self.capacity #Movemos front al indice anterior de forma circular. Ejemplo: front = 1 capacity = 5. (1-1+5)%5 = 0 -> front = 0. Se inserta en la posicion 0. Si front = 0, (0-1+5)%5 = 4 -> front = 4. Se inserta en la posicion 4
        self.deque[self.front] = data #Agregamos el dato en la posicion de front porque front es el indice del primer elemento en el deque
        
    def addRear(self, data): #Agrega un elemento al final del deque
        if self.isFull(): #Si el deque esta lleno
            raise Exception("El deque esta lleno, no se puede agregar un elemento al final") 
            
        if self.isEmpty(): #Si el deque esta vacio
            self.front = 0 #Hacemos que front apunte al primer indice
            self.rear = 0 #Hacemos que rear apunte al primer indice
        else:
            self.rear = (self.rear + 1) % self.capacity #Movemos rear al siguiente indice de forma circular. Ejemplo rear = 3, capacity = 5. (3+1)%5 = 4 -> rear = 4. Se inserta en la posicion 4. Si rear = 4, (4+1)%5 = 0 -> rear = 0. Se inserta en la posicion 0
        self.deque[self.rear] = data #Agregamos el dato en la posicion de rear porque rear es el indice del ultimo elemento en el deque
        
    def removeFront(self): #Elimina un elemento del frente del deque
        if self.isEmpty(): 
            raise Exception("El deque esta vacio, no se puede eliminar un elemento del frente")
        data = self.deque[self.front] #Guardamos el dato que apunta front pues es el primer elemento en el deque (FIFO)
        self.deque[self.front] = None #Eliminamos el elemento del deque asignando None en la posicion de front
        self.front = (self.front + 1) % self.capacity #Movemos front al siguiente indice de forma circular
            
        if self.front == (self.rear + 1) % self.capacity: #Si el deque queda vacio despues de eliminar el elemento
            self.front = -1 #Hacemos que front y rear apunten a -1
            self.rear = -1
                
        return data #Regresamos el dato que se elimino
    
    def removeRear(self): #Elimina un elemento del final del deque
        if self.isEmpty(): 
            raise Exception("El deque esta vacio, no se puede eliminar un elemento del final")
        data = self.deque[self.rear] #Guardamos el dato que apunta rear pues es el ultimo elemento en el deque (LIFO)
        self.deque[self.rear] = None #Eliminamos el elemento del deque asignando None en la posicion de rear
        self.rear = (self.rear - 1 + self.capacity) % self.capacity #Movemos rear al indice anterior de forma circular
            
        if self.front == (self.rear + 1) % self.capacity: #Si el deque queda vacio despues de eliminar el elemento
            self.front = -1 #Hacemos que front y rear apunten a -1
            self.rear = -1
                
        return data #Regresamos el dato que se elimino
    
    def peekFront(self): #Muestra el elemento del frente del deque sin eliminarlo
        if self.isEmpty():
            raise Exception("El deque esta vacio, no se puede mostrar el elemento del frente")
        return self.deque[self.front] #Regresamos el dato que apunta front sin eliminarlo
    
    def peekRear(self): #Muestra el elemento del final del deque sin eliminarlo
        if self.isEmpty():
            raise Exception("El deque esta vacio, no se puede mostrar el elemento del final")
        return self.deque[self.rear] #Regresamos el dato que apunta rear sin eliminarlo
    
    def __str__(self):
        return "Deque: " + str(self.deque) + " Front: " + str(self.front) + " Rear: " + str(self.rear)
    
myDeque = Deque(5) #Creamos una instancia de la clase Deque con capacidad 5

myDeque.addRear(10) #Agregamos elementos al final del deque
myDeque.addRear(20)
myDeque.addFront(5) #Agregamos elementos al frente del deque
myDeque.addFront(1)
print(myDeque) #Mostramos el deque

print("Saco del front:", myDeque.removeFront())  # 1 o 5 según el orden
print("Saco del rear:", myDeque.removeRear())    # 20
print("Estado actual:", myDeque)

        