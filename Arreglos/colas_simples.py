class Queue:
    def __init__(self, capacity):
        self.capacity = capacity              
        self.queue = [None] * capacity        
        self.front = 0                        
        self.rear = -1                        

    def is_empty(self):
        # Si rear < front, no hay elementos válidos
        return self.rear < self.front

    def is_full(self):
        # Si rear alcanza la última posición, está llena
        return self.rear == self.capacity - 1

    def enqueue(self, item):
        if self.is_full():
            raise Exception("La cola está llena, no se puede agregar el elemento.")
        self.rear += 1
        self.queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception("La cola está vacía, no se puede eliminar ningún elemento.")
        front_item = self.queue[self.front]
        self.front += 1
        return front_item

    def show(self):
        if self.is_empty():
            raise Exception("La cola está vacía.")
        print("Elementos en la cola:", end=" ")
        for i in range(self.front, self.rear + 1):
            print(self.queue[i], end=" ")
        print()


my_queue = Queue(5)

my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)
my_queue.show()

print("Elemento al frente que borraremos:", my_queue.peek())

my_queue.dequeue()
my_queue.show()

print("Se agregarán dos elementos...")
my_queue.enqueue(40)
my_queue.enqueue(50)
my_queue.show()
