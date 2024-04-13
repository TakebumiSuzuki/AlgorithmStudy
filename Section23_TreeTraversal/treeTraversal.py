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
    
    def BFS(self):
        if self.root is None: return None;
        
        tempNodes = [self.root];
        result = [];
        
        def recursion(currentNode):
            result.append(currentNode.value);
            if currentNode.left: tempNodes.append(currentNode.left);
            if currentNode.right: tempNodes.append(currentNode.right);
                
            tempNodes.pop(0);
            if len(tempNodes) == 0: return;
            currentNode = tempNodes[0];
            recursion(currentNode);
            
        recursion(self.root);
        return result;
    
    def DFSPreOrder(self):
        result = []
        if self.root is None: return result
        
        def recursion(currentNode):
            result.append(currentNode.value)
            if currentNode.left: recursion(currentNode.left)
            if currentNode.right: recursion(currentNode.right)
        
        recursion(self.root)
        return result
    
    def DFSPostOrder(self):
        result = []
        if self.root is None: return result
        
        def recursion(currentNode):
            if currentNode.left: recursion(currentNode.left)
            if currentNode.right: recursion(currentNode.right)
            result.append(currentNode.value)
        
        recursion(self.root)
        return result
    
    def DFSInOrder(self):
        result = []
        if self.root is None: return result
        
        def recursion(currentNode):
            if currentNode.left: recursion(currentNode.left)
            result.append(currentNode.value)
            if currentNode.right: recursion(currentNode.right)
            
        recursion(self.root)
        return result
        
        
BST = BinarySearchTree()
BST.insert(10);
BST.insert(6);
BST.insert(15);
BST.insert(3);
BST.insert(8);
BST.insert(20);
print(BST.DFSInOrder());
            


    