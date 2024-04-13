class Node:
    def __init__(self, value):
        self.val = value;
        self.next = None;
        
#push, Shift, Unshiftは軽量の作業。しかしpopは必ず最後までtraverseが必要になる。
#また、getもその場所までtraverseしないといけない。この為、getを使うset,insert,removeもtraverseが必要となる。
class SinglyLinkedList: 
    def __init__(self):
        self.head = None;
        self.tail = None;
        self.length = 0;
    
    def push(self, value):
        newNode = Node(value);
        if self.length == 0:
            self.head = newNode;
        else:
            self.tail.next = newNode;
        self.tail = newNode; 
        self.length += 1;
        return self
    
    def pop(self):
        node = self.head
        if node is None:
            return None;
        if node.next is None:
            self.head = None;
            self.tail = None;
            self.length = 0;
            return node
        
        while node.next.next is not None:
            node = node.next;
            
        popNode = node.next
        node.next = None;
        self.tail = node;
        self.length -= 1;
        return popNode;
    
    def shift(self):
        if self.head is None:
            return None;
        popHead = self.head;
        self.head = self.head.next;
        self.length -= 1;
        if self.head is None:
            self.tail = None;
        return popHead;
    
    def unshift(self,val):
        newNode = Node(val);
        if self.head is None:
            self.head = newNode;
            self.tail = newNode;
            self.length += 1;
        else:
            newNode.next = self.head;
            self.head = newNode;
            self.length += 1;
        return self;
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None;
        
        counter = 0
        node = self.head;
        while counter != index:
            node = node.next;
            counter += 1
        return node
    
    def set(self, index, value):
        result = self.get(index);
        if result is None:
            return False
        else:
            result.val = value;
            return True;
        
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False;
        elif index == self.length:
            self.push(value);
            return True;
        elif index == 0:
            self.unshift(value);
            return True;
        else:
            prevNode = self.get(index - 1);
            currentNode = prevNode.next
            newNode = Node(value);
            prevNode.next = newNode;
            newNode.next = currentNode;
            self.length += 1;
            return True;
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return False;
        elif index == 0:
            return self.shift();
        elif index == self.length - 1:
            return self.pop();
        else:
            prevNode = self.get(index - 1);
            current = prevNode.next;
            nextNode = current.next;
            prevNode.next = nextNode;
            self.length -= 1;
            return current;
    
    def reverse(self):
        first = self.head;
        second = first.next;
        third = second.next;
        while True:
            second.next = first;
            first = second;
            second = third;
            if third.next is None:
                second.next = first;
                break;
            third = third.next;
        temp = self.head;
        self.head = self.tail;
        self.tail = temp;
        return self;
            
    
        
myList = SinglyLinkedList();
myList.push("myFirst")
myList.push("mySecond")
myList.push("myThird")
myList.push("myFourth")
myList.push("!")

print(myList.reverse());
print(myList.get(0).val)
print(myList.get(1).val)
print(myList.get(2).val)
print(myList.get(3).val)
print(myList.get(4).val)

# print(myList.shift().val)
# print(myList.length)
# print(myList.shift().val)
# print(myList.length)
# print(myList.shift().val)
# print(myList.length)
# print(myList.shift().val)
# print(myList.length)
# print(myList.shift().val)
# print(myList.length)
# print(myList.shift())



# print("1回目のpush始まります")
# print(myList.pop().val)
# print(myList.tail.val)
# print("２回目のpush始まります")
# print(myList.pop().val)
# print(myList.tail.val)
# print("３回目のpush始まります")
# print(myList.pop().val)
# print(myList.tail.val)
# print("４回目のpush始まります")
# print(myList.pop().val)
# print(myList.tail.val)
# print("５回目のpush始まります")
# print(myList.pop().val)
# print(myList.tail)
# print("６回目のpush始まります")
# print(myList.pop())
# print(myList.tail)
        
        
        
            
