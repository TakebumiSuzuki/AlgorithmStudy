#BSTはon the flyでsortしながらデータ構造を作り上げる。そのinsertionもsearchも Log N

#Arrayをベースとしたsorted data上でのBinary Searchは Log N
#ArrayをベースとしたArrayをソートするのに、Merge Sortを使うと N Log N

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

        

BST = BinarySearchTree()  
BST.insert(50)
BST.insert(15)
BST.insert(80)
BST.insert(100)
BST.insert(3)
print(BST.find(10))
print(BST.find(3))
print(BST.find(17))
print(BST.find(50))

       
        
        
            
        
        