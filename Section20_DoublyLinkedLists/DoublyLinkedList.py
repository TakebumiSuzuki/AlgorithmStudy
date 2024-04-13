class Node:
    def __init__(self, val):
        self.val = val;
        self.next = None;
        self.prev = None;
        
#push, Shift, Unshift,popすべてが軽量。getその場所までtraverseが必要だがsinglyLinkedListの半分の作業量で良い。
#getを使うset,insert,removeもtraverseが必要。
class DoublyLinkedList:
    def __init__(self):
        self.head = None;
        self.tail = None;
        self.length = 0;
        
    def push(self, val):
        newNode = Node(val);
        if self.head is None:
            self.head = newNode;
        else:
            currentTail = self.tail;
            currentTail.next = newNode;
            newNode.prev = currentTail;
        self.tail = newNode;
        self.length += 1; 
        return self;
    
    def pop(self):
        if self.length == 0:
            return None;
        currentTail = self.tail;
        if self.length == 1:
            self.head = None;
            self.tail = None;
        else:
            newTail = currentTail.prev;
            newTail.next = None;
            self.tail = newTail; 
            currentTail.prev = None;
        self.length -= 1;
        return currentTail
    
    def shift(self):
        if self.length == 0:
            return self;
        oldHead = self.head
        if self.length == 1:
            self.head  = None;
            self.tail  = None;
            self.length = 0;
            return oldHead
        
        self.head = self.head.next;
        self.head.prev = None;
        self.length -= 1;
        oldHead.next = None;
        return oldHead
        
    def unshift(self, val):
        newNode = Node(val);
        if self.length == 0:
            self.head = newNode;
            self.tail = newNode;
        else:
            currentHead = self.head;
            self.head = newNode;
            self.head.next = currentHead;
            currentHead.prev = self.head;
            
        self.length += 1;
        return self;
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None;
        
        if index < (self.length // 2):
            tempNode = self.head;
            for i in range(index):
                tempNode = tempNode.next;
        else:
            tempNode = self.tail;
            for i in range(self.length - index - 1):
                tempNode = tempNode.prev;
        return tempNode;
                
    def set(self, index, val):
        node = self.get(index);   
        if node is None:
            return None;
        node.val = val;
        return True;
    
    def insert(self, index, val):
        newNode = Node(val);
        currentNode = self.get(index);
        if index == self.length:
            self.push(val);
            return True; 
        if index == 0:
            self.unshift(val);
            return True;
        if currentNode is None:
            return False;
        
        prevNode = currentNode.prev;
        prevNode.next = newNode;
        newNode.prev = prevNode;
        newNode.next = currentNode;
        currentNode.prev = newNode;
        self.length += 1;
        return True
        
    def remove(self,index):
        if self.length == 0:
            return None;
        if index == 0:
            return self.shift();
        if index == self.length - 1:
            return self.pop();
        currentNode = self.get(index);
        if currentNode is None:
            return None;
        prevNode = currentNode.prev;
        nextNode = currentNode.next;
        prevNode.next = nextNode;
        nextNode.prev = prevNode;
        currentNode.next = None;
        currentNode.prev = None;
        self.length -= 1;
        return currentNode; 
    
    def reverse(self):
        tempHead = self.head;
        self.head = self.tail;
        self.tail = tempHead;
        count = 0;
        
        current = self.head;
        while count >= 0 and count < self.length:
            
            if count == 0:
                current.next = current.prev;
                current.prev = None;
                current = current.next;
            elif count == self.length - 1:
                current.prev = current.next;
                current.next = None;
            else:
                tempNext = current.next;
                current.next = current.prev;
                current.prev = tempNext;
                current = current.next;
            count += 1;
                
        return self;
        

doublyLinkedList = DoublyLinkedList();
doublyLinkedList.push(5).push(10).push(15).push(20)
doublyLinkedList.reverse(); # singlyLinkedList;
print(doublyLinkedList.length); # 4
print(doublyLinkedList.head.val); # 20
print(doublyLinkedList.head.next.val); # 15
print(doublyLinkedList.head.next.next.val); # 10
print(doublyLinkedList.head.next.next.next.val); # 5
        
        