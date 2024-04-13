class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return self
        currentNode = self.root
        while True:
            if value <= currentNode.value:
                if currentNode.left is None:
                    currentNode.left = newNode
                    return self
                currentNode = currentNode.left
            else:
                if currentNode.right is None:
                    currentNode.right = newNode
                    return self
                currentNode = currentNode.right
                
    def find(self, value):
        if self.root is None: return None
        currentNode = self.root
        while currentNode is not None: 
            currentValue = currentNode.value
            if currentValue < value:
                currentNode = currentNode.right
            elif currentValue > value:
                currentNode = currentNode.left
            else:
                return currentNode
        return None
    
    def DFSPreOrder(self):
        if self.root is None: return []
        result = []
        nodeCue = [self.root]
        while nodeCue != []:
            currentNode = nodeCue.pop()
            result.append(currentNode.value)
            if currentNode.right is not None:
                nodeCue.append(currentNode.right)
            if currentNode.left is not None:
                nodeCue.append(currentNode.left)
        return result
            
    def DFSInOrder(self):
        if self.root is None: return []
        result = []
        nodeStack = [self.root]
        while len(nodeStack) != 0:
            if currentNode is None:
                parentNode = nodeStack.pop()
                result.append(nodeStack.pop().value)
                currentNode = parentNode.right
                
                if currentNode.right is not None:
                    nodeStack.append(currentNode.right)
            else:
                nodeStack.append(currentNode.left)
        return result
    
    # def DFSInOrder(self):
    #     if self.root is None:
    #         return []
    #     result = []
    #     nodeStack = []
    #     currentNode = self.root
    #     while nodeStack or currentNode:
    #         if currentNode:
    #             nodeStack.append(currentNode)
    #             currentNode = currentNode.left
    #         else:
    #             currentNode = nodeStack.pop()
    #             result.append(currentNode.value)
    #             currentNode = currentNode.right
    #     return result

        
        
    # def DFSPostOrder(self):
        
    
        
binarySearchTree = BinarySearchTree()
binarySearchTree.insert(15).insert(20).insert(10).insert(12).insert(1).insert(5).insert(50)
print(binarySearchTree.DFSInOrder())  # [15, 10, 1, 5, 12, 20, 50]


 