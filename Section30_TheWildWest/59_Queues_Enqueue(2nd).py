class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        
    def enqueue(self, val):
        newNode = Node(val)
        if self.size == 0:
            self.first = newNode
        else:
            self.last.next = newNode
        self.last = newNode
        self.size += 1
        return self.size
    
queue = Queue()

queue.enqueue(10)  # 1
print(queue.size)  # 1
queue.enqueue(100)  # 2
print(queue.size)  # 2
queue.enqueue(1000)  # 3
print(queue.size)  # 3
