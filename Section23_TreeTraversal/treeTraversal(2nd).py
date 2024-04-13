class Node:
    def __init__(self, value):
        self.value = value;
        self.left = None;
        self.right = None;

class BinarySearchTree:
    def __init__(self):
        self.root = None;
        
    def insert(self, val):
        newNode = Node(val)
        if self.root is None:
            self.root = newNode
            return
        
        def helper(node):
            if val >= node.value:
                if node.right is None:
                    node.right = newNode
                else:
                    helper(node.right)
            else:
                if node.left is None:
                    node.left = newNode
                else:
                    helper(node.left)
        helper(self.root)
        
        
    def find(self, val):
        if self.root is None:
            return False
        currentNode = self.root
        while True:
            if val > currentNode.value:
                if currentNode.right is None:
                    return False
                currentNode = currentNode.right
            elif val < currentNode.value:
                if currentNode.left is None:
                    return False
                currentNode = currentNode.left
            else:
                return True
    
    def BFS(self):
        if self.root is None:
            return None
        queue = [self.root]
        result = []
        while len(queue) != 0:
            tempNode = queue.pop(0)
            result.append(tempNode.value)
            if tempNode.left is not None:
                queue.append(tempNode.left)
            if tempNode.right is not None:
                queue.append(tempNode.right)
        return result
    
    def DFS_PreOrder(self):
        if self.root is None: return None
        result = []
        def traverse(node):
            result.append(node.value)
            if node.left:
                traverse(node.left)
            if node.right:
                traverse(node.right)
        
        traverse(self.root)
        return result
    
    
    def DFS_PostOrder(self):
        if self.root is None: return None
        result = []
        def traverse(node):
            if node is None: return
            if node.left is None and node.right is None:
                result.append(node.value)
                return
            traverse(node.left)
            traverse(node.right)
            result.append(node.value)
        traverse(self.root)
        return result
    
    def DFS_FirstInOrder(self):
        if self.root is None: return None
        result = []
        def traverse(node):
            if node.left:
                traverse(node.left)
            result.append(node.value)
            if node.right:
                traverse(node.right)
        traverse(self.root)
        return result
        
        
        
        

BST = BinarySearchTree()  
BST.insert(50)
BST.insert(15)
BST.insert(80)
BST.insert(100)
BST.insert(3)
print(BST.DFS_FirstInOrder())