class Node:
    def __init__(self, priority, val = ""):
        self.priority = priority
        self.val = val
        

class PriorityQueue:
    def __init__(self):
        self.values = []
        
    def enqueue(self, priority, val = ""):
        newNode = Node(priority, val)
        self.values.append(newNode)
        
        def recursive(idx):
            if idx == 0:
                return
            parentIdx = (idx + 1) // 2 - 1
            if self.values[parentIdx].priority <= priority:
                return
            self.values[idx] = self.values[parentIdx]
            self.values[parentIdx] = newNode
            
            recursive(parentIdx)
            
        recursive(len(self.values) - 1)
        
        
    def dequeue(self):
        if len(self.values) == 0: return None
        firstNode = self.values[0]
        lastNode = self.values[len(self.values) - 1]
        self.values[0] = lastNode
        self.values.pop()
        if len(self.values) == 0: return firstNode
        newTopNode = self.values[0]
        priority = newTopNode.priority

        def recursive(currentIdx):
            leftIdx = (currentIdx + 1) * 2 - 1
            rightIdx = leftIdx + 1
            swapIdx = 0
            if leftIdx < len(self.values):
                leftPriority = self.values[leftIdx].priority
                if rightIdx >= len(self.values) and leftPriority < priority:
                    swapIdx = leftIdx
                elif rightIdx < len(self.values):
                    rightPriority = self.values[rightIdx].priority
                    if leftPriority <= rightPriority and leftPriority < priority:
                        swapIdx = leftIdx
                    if rightPriority <= leftPriority and rightPriority < priority:
                        swapIdx = rightIdx
            if swapIdx != 0:    
                self.values[currentIdx] = self.values[swapIdx]
                self.values[swapIdx] = newTopNode
                recursive(swapIdx)
            
        recursive(0)
        
        return firstNode

        
        
        
        
        
bh = PriorityQueue()
bh.enqueue(5)
bh.enqueue(1)
bh.enqueue(4)
bh.enqueue(2)
bh.enqueue(3)
print(bh.values[0].priority)
print(bh.values[1].priority)
print(bh.values[2].priority)
print(bh.values[3].priority)
print(bh.values[4].priority)
print('------')
bh.dequeue()
print(bh.values[0].priority)
print(bh.values[1].priority)
print(bh.values[2].priority)
print(bh.values[3].priority)
print('------')
bh.dequeue()
print(bh.values[0].priority)
print(bh.values[1].priority)
print(bh.values[2].priority) 
print('------')
bh.dequeue()
print(bh.values[0].priority)
print(bh.values[1].priority)
print('------')
bh.dequeue()
print(bh.values[0].priority)
print('------')
bh.dequeue()

        
    
    
    
        