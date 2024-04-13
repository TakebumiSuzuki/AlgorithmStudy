class Node:
    def __init__(self, value):
        self.value = value;
        self.left = None;
        self.right = None;

class BinarySearchTree:
    def __init__(self):
        self.root = None;
        
    def insert(self, value):
        newNode = Node(value);
        if self.root is None:
            self.root = newNode;
            return self
        
        currentNode = self.root;
        while True:
            if currentNode.value > value:
                if currentNode.left is None:
                    currentNode.left = newNode;
                    return self
                currentNode = currentNode.left;
            elif currentNode.value < value:
                if currentNode.right is None:
                    currentNode.right = newNode;
                    return self
                currentNode = currentNode.right; 
            else:
                return False;
                
                
    def insertRecursively(self, value):
        newNode = Node(value);
        if self.root is None:
            self.root = newNode;
            return self
        
        currentNode = self.root;
        def recursive(currentNode):
            if currentNode.value > newNode.value:
                if currentNode.left is None:
                    currentNode.left = newNode;
                    return self;
                else:
                    currentNode = currentNode.left;
            elif currentNode.value < value:
                if currentNode.right is None:
                    currentNode.right = newNode;
                    return self;
                else:
                    currentNode = currentNode.right;
            else:
                return False
            recursive(currentNode);
        
        recursive(currentNode);
        
    def find(self,value):
        if self.root is None:
            return False
        
        currentNode = self.root;
        while True:
            if currentNode.value > value:
                if currentNode.left is None:
                    return False
                currentNode = currentNode.left;
            elif currentNode.value < value:
                if currentNode.right is None:
                    return False
                currentNode = currentNode.right; 
            else:
                return True;
        
        
         
                
BST = BinarySearchTree()
BST.insert(10);
BST.insert(5);
BST.insert(7);
BST.insert(2);
BST.insert(6);
print(BST.find(3))
print(BST.find(7))
print(BST.find(2))
print(BST.find(11))
print(BST.find(7))
print(BST.find(1))

        
            

        