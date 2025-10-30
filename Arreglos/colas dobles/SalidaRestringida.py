class OutputRestrictedDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.deque = [None] * capacity  #Definimos el tamaño del arreglo inicializado con None en cada posición
        self.front = -1 #Los indices empiezan en -1
        self.rear = -1
        
    def isEmpty(self):
        return self.front == -1 #Si el indice del frente es -1, la cola está vacía
    
    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front #Si el siguiente índice del rear es igual al front, la cola está llena ej: Front = 3 (4+1)%5 == 0 (Da false, no esta llena) o (2+1)%5 == 3 (da true, esta llena)
    
    def insertFront(self, data):
        if self.isFull():
            raise Exception("Deque is full")
        if self.isEmpty():
            self.front = 0 #Si la cola está vacía, hacemos que front y rear apunten al primer índice
            self.rear = 0
        else:
            self.front = (self.front - 1 + self.capacity) % self.capacity #Decrementamos el índice del front circularmente ej: (0-1+5)%5 == 4 o (3-1+5)%5 == 2
        self.deque[self.front] = data #Asignamos el valor en la posición del front
        return data
    
    def insertRear(self, data):
        if self.isFull():
            raise Exception("Deque is full")
        if self.isEmpty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity #Incrementamos el índice del rear circularmente ej: (-1+1)%5 == 0 o (0+1)%5 == 1
        self.deque[self.rear] = data #Asignamos el valor en la posición del rear
        return data
    
    def deleteFront(self):
        if self.isEmpty():
            raise Exception("Deque is empty")
        data = self.deque[self.front] #Guardamos el valor que vamos a eliminar
        if self.front == self.rear: #Si solo hay un elemento
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity #Incrementamos el índice del front circularmente ej: (0+1)%5 == 1 o (4+1)%5 == 0
        return data #Devolvemos el valor eliminado

    def show(self):
        if self.isEmpty():
            print("Deque is empty")
            return
        i = self.front
        while True:
            print(self.deque[i], end=", ")
            if i == self.rear: #Rompe el ciclo cuando i llegue a rear, osease al ultimo elemento en la cola
                break
            i = (i + 1) % self.capacity #Movemos i al siguiente indice de forma circular
        print()


print("Podemos insertar por ambos lados pero eliminar solo por el frente")        
myDeque = OutputRestrictedDeque(3) #Creamos una instancia de la clase OutputRestrictedDeque con capacidad 5

myDeque.insertRear(1) #Agregamos elementos a la 
myDeque.show() #Mostramos la lista que representa la cola
print("Agregamos por rear:", myDeque.insertRear(2))
myDeque.show()
print("Agregamos por front:", myDeque.insertFront(3))
myDeque.show()
print("Elemento eliminado por Front:", myDeque.deleteFront()) #Eliminamos el primer elemento
myDeque.show()

    
    
        