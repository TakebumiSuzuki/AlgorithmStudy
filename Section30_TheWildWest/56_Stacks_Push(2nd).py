class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0
        
    def push(self, val):
        newNode = Node(val)
        if self.size != 0:
            newNode.next = self.first
        else:
            self.last = newNode
        self.first = newNode
        self.size += 1
        return self.size
    
    def pop(self):
        if self.size == 0:
            return None
        firstNode = self.first
        if self.size == 1:
            self.first = None
            self.last = None
        self.first = firstNode.next
        self.size -= 1
        return firstNode.value
    
    
stack = Stack()
stack.push(10)
stack.push(100)
stack.push(1000)
removed = stack.pop()
print(removed)  # 1000
print(stack.size)  # 2
stack.pop()
stack.pop()
print(stack.size)  # 0
       
        
# # スタックの使い方の例
# stack = Stack()
# print(stack.push(10))  # 1
# print(stack.first.value)  # 10
# print(stack.last.value)  # 10
# print(stack.push(100))
# print(stack.first.value)  # 100
# print(stack.last.value)  # 10
# print(stack.push(1000))
# print(stack.first.value)  # 1000
# print(stack.last.value)  # 10

# stack = Stack()

# print(stack.push(10))  # 1
# print(stack.size)  # 1
# print(stack.push(100))  # 2
# print(stack.size)  # 2
# print(stack.push(1000)) # 3
# print(stack.size)  # 3

        