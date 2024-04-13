class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
    
    def push(self, val):
        newNode = Node(val)
        if self.length == 0:
            self.head = newNode
        elif self.length == 1:
            self.head.next = newNode
        else:
            self.tail.next = newNode
        self.tail = newNode
        self.length += 1
        return self
    
    def pop(self):
        if self.length == 0: 
            return None
        lastNode = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
            return lastNode
        
        tempNode = self.head
        for i in range(self.length - 2):
            tempNode = tempNode.next
        tempNode.next = None
        self.tail = tempNode
        self.length -= 1
        return lastNode 
    
    def get(self, index):
        if index >= self.length or index < 0: 
            return None
        currentNode = self.head
        for i in range(index):
            currentNode = currentNode.next
        return currentNode
        
    def insert(self, index, val):
        newNode = Node(val)
        if index > self.length or index < 0: 
            return False
        if index == self.length:
            self.tail.next = newNode
            self.tail = newNode
        elif index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            prevNode = self.get(index - 1)
            nextNode = prevNode.next
            newNode.next = nextNode
            prevNode.next = newNode
        self.length += 1
        return True
    
    def rotate(self, index):
        index = index % self.length
        if index == 0:
            return self
        if index < 0:
            index = index + self.length
        self.tail.next = self.head
        newTail = self.get(index - 1)
        newHead = newTail.next
        self.tail = newTail
        self.head = newHead
        newTail.next = None
        return self
    
    def set(self, index, val):
        if index < 0 or index > self.length:
            return False
        if index == self.length:
            self.push(val)
            return True
        newNode = Node(val)
        if index == 0:
            newNode.next = self.head
            self.head = newNode
        else:
            prevNode = self.get(index - 1)
            nextNode = prevNode.next
            newNode.next = nextNode
            prevNode.next = newNode
        self.length += 1
        return True
        
        
singlyLinkedList = SinglyLinkedList()
 
print(singlyLinkedList.set(0,10)) # true
print(singlyLinkedList.set(1,2)) # true
print(singlyLinkedList.length) # 2
print(singlyLinkedList.head.val) # 10
 
print(singlyLinkedList.set(10,10)) # false
print(singlyLinkedList.set(1,100))
print(singlyLinkedList.head.next.next.val)
        
        
            
# singlyLinkedList = SinglyLinkedList()
# singlyLinkedList.push(5).push(10).push(15).push(20).push(25); # singlyLinkedList

# print(singlyLinkedList.head.val); # 5
# print(singlyLinkedList.tail.val); # 25;
 
# singlyLinkedList.rotate(3);
# print(singlyLinkedList.head.val); # 20
# print(singlyLinkedList.head.next.val); # 25
# print(singlyLinkedList.head.next.next.val); # 5
# print(singlyLinkedList.head.next.next.next.val); # 10
# print(singlyLinkedList.head.next.next.next.next.val); # 15
# print(singlyLinkedList.tail.val); # 15
# print(singlyLinkedList.tail.next); # null

# singlyLinkedList = SinglyLinkedList();
# singlyLinkedList.push(5).push(10).push(15).push(20).push(25);
# print(singlyLinkedList.head.val); # 5
# print(singlyLinkedList.tail.val); # 25;
 
# print(singlyLinkedList.rotate(-1));
# print(singlyLinkedList.head.val); # 25
# print(singlyLinkedList.head.next.val); # 5
# print(singlyLinkedList.head.next.next.val); # 10
# print(singlyLinkedList.head.next.next.next.val); # 15
# print(singlyLinkedList.head.next.next.next.next.val); # 20
# print(singlyLinkedList.tail.val); # 20
# print(singlyLinkedList.tail.next) # null

# singlyLinkedList = SinglyLinkedList();
# singlyLinkedList.push(5).push(10).push(15).push(20).push(25);
# print(singlyLinkedList.head.val); # 5
# print(singlyLinkedList.tail.val); # 25;
 
# singlyLinkedList.rotate(1000);
# print(singlyLinkedList.head.val); # 5
# print(singlyLinkedList.head.next.val); # 10
# print(singlyLinkedList.head.next.next.val); # 15
# print(singlyLinkedList.head.next.next.next.val); # 20
# print(singlyLinkedList.head.next.next.next.next.val); # 25
# print(singlyLinkedList.tail.val); # 25
# print(singlyLinkedList.tail.next) # null