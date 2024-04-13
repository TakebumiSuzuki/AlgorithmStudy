class Node:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        
class PriorityQueue:
    def __init__(self):
        self.values = []
        
    def enqueue(self, val, priority):
        newNode = Node(val, priority)
        values = self.values
        self.values.append(newNode)
        if len(values) == 1: return
        currentIdx = len(values) - 1
        def bubbleUp():
            nonlocal currentIdx
            parentIdx = (currentIdx - 1) // 2
            if parentIdx < 0 : return
            if values[parentIdx].priority <= priority:
                return
            else:
                temp = values[parentIdx]
                values[parentIdx] = newNode
                values[currentIdx] = temp
                currentIdx = parentIdx
                bubbleUp()
        bubbleUp()
        return
    
    def dequeue(self):
        values = self.values
        if len(values) == 0: return None
        if len(values) == 1: return self.values.pop()
        
        lastNode = values.pop()
        lastPriority = lastNode.priority
        returnNode = values[0]
        values[0] = lastNode
        currentIdx = 0
        def swap(idx1, idx2):
            temp = values[idx1]
            values[idx1] = values[idx2]
            values[idx2] = temp
        
        def bubbleDown():
            nonlocal currentIdx
            nextLeftIdx = currentIdx * 2 + 1
            nextRightIdx = currentIdx * 2 + 2
            
            if nextLeftIdx < len(values) and nextRightIdx >= len(values) :
                if values[nextLeftIdx].priority < lastPriority:
                    swap(nextLeftIdx, currentIdx)
                return returnNode
            elif nextLeftIdx < len(values) and nextRightIdx < len(values) :
                if values[nextLeftIdx].priority > values[nextRightIdx].priority:
                    if lastPriority > values[nextRightIdx].priority:
                        swap(nextRightIdx, currentIdx)
                        currentIdx = nextRightIdx
                        bubbleDown()
                if values[nextLeftIdx].priority < values[nextRightIdx].priority:  
                    if  lastPriority > values[nextLeftIdx].priority:  
                        swap(nextLeftIdx, currentIdx)
                        currentIdx = nextLeftIdx
                        bubbleDown()
            else:
                return returnNode
        bubbleDown()
                        
        
                
            
                    
                
            

    
bh = PriorityQueue()
bh.enqueue(5, 10)
bh.enqueue(1, 8)
bh.enqueue(4, 1)
bh.enqueue(2, 3)
bh.enqueue(3, 7)
bh.dequeue()
bh.dequeue()
bh.dequeue()
bh.dequeue()
bh.dequeue()
print(bh.values)
# print(bh.values[0].priority)
# print(bh.values[1].priority)
# print(bh.values[2].priority)
# print(bh.values[3].priority)
# print(bh.values[4].priosrity)
             
# 1,3,8,10,7  
# 7,3,8,10
# 3,7,8,10 
# ７、１０、８

            
            
        
        
        
        
        
    