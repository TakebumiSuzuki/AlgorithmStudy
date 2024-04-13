class MaxBinaryHeap():
    def __init__(self):
        self.values = []
        
    def insert(self,element):
        self.values.append(element)
        
        def recursion(idx):
            if idx == 0:
                return
            parentIdx = ((idx + 1) // 2) - 1
            parent = self.values[parentIdx]
            if parent >= element:
                return
            else:
                self.values[idx] = parent
                self.values[parentIdx] = element
                recursion(parentIdx)
                
        recursion(len(self.values) - 1);
        
    def extractMax(self):
        if len(self.values) == 0: return None;
        max = self.values[0]
        if len(self.values) == 1: return max
        end = self.values.pop()
        
        self.values[0] = end
        
        def recursion(idx):
            leftChildIdx = (idx + 1) * 2 - 1
            if leftChildIdx >= len(self.values):
                return max
            leftChild = self.values[leftChildIdx]
            
            rightChildIdx = leftChildIdx + 1
            if rightChildIdx >= len(self.values):
                if leftChild > end:
                    self.values[idx] = leftChild
                    self.values[leftChildIdx] = end
                return max
                
            rightChild = self.values[rightChildIdx]
            if leftChild >= rightChild and leftChild > end:
                self.values[idx] = leftChild
                self.values[leftChildIdx] = end
                return recursion(leftChildIdx)
            elif leftChild < rightChild and rightChild > end:
                self.values[idx] = rightChild
                self.values[rightChildIdx] = end
                return recursion(rightChildIdx)
            else:
                return max
            
        return recursion(0)
        
            
            
            
            
        
        
        
bh = MaxBinaryHeap()
bh.insert(41)
bh.insert(39)
bh.insert(18)
bh.insert(27)
bh.insert(12)
bh.insert(55)
print(bh.values)
print(bh.extractMax())
print(bh.values)


        
