class InputRestrictedDeque:
    def __init__(self, capacity):
        self.capacity = capacity
        self.deque = [None] * capacity  #Definimos el tamaño del arreglo
        self.front = -1 #Los indices empiezan en -1
        self.rear = -1
        
    def isEmpty(self):
        return self.front == -1 #Si el indice del frente es -1, la cola está vacía
    
    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front #Si el siguiente índice del rear es igual al front, la cola está llena ej: (4+1)%5 == 0 o (2+1)%5 == 3
    
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
    
    def deleteRear(self):
        if self.isEmpty():
            raise Exception("Deque is empty")
        data = self.deque[self.rear] #Guardamos el valor que vamos a eliminar
        if self.front == self.rear: #Si solo hay un elemento
            self.front = -1
            self.rear = -1
        else:
            self.rear = (self.rear - 1 + self.capacity) % self.capacity #Decrementamos el índice del rear circularmente ej: (0-1+5)%5 == 4 o (3-1+5)%5 == 2
        return data #Devolvemos el valor eliminado
    
    def show(self):
        if self.isEmpty():
            print("Deque is empty")
            return
        i = self.front
        while True:
            print(self.deque[i], end=", ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()

print("Solo podemos insertar por el rear pero eliminar por ambos extremos")
myDeque = InputRestrictedDeque(5) #Creamos una instancia de la clase InputRestrictedDeque con capacidad 5
myDeque.insertRear(10) #Insertamos elementos en el rear
myDeque.insertRear(20)
myDeque.show() #Mostramos los elementos del deque
print("Insertado desde rear:", myDeque.insertRear(30))
myDeque.show() #Mostramos los elementos del deque
print("Eliminamos desde Front:", myDeque.deleteFront()) #Eliminamos un elemento del front
myDeque.show() #Mostramos los elementos del deque
print("Eliminamos desde Rear:", myDeque.deleteRear()) #Eliminamos un elemento del rear
myDeque.show() #Mostramos los elementos del deque