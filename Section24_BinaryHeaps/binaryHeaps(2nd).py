class MaxBinaryHeap:
    def __init__(self):
        self.values = []
        
    def insert(self, element):
        currentIdx = len(self.values)
        self.values.append(element)
        
        def swap():
            nonlocal currentIdx
            parentIdx = (currentIdx - 1) // 2
            if parentIdx < 0:
                return
            if element > self.values[parentIdx]:
                temp = self.values[parentIdx]
                self.values[parentIdx] = element
                self.values[currentIdx] = temp
                currentIdx = parentIdx
                swap()
        swap()
        return self.values
    
    def extractMax(self):
        heapArr = self.values
        if len(heapArr) == 0: return None
        if len(heapArr) == 1: return heapArr.pop(), []
        
        maxValue = heapArr[0]
        lastValue = heapArr.pop()
        heapArr[0] = lastValue
        tempIdx = 0
        def sinkDown():
            nonlocal tempIdx
            nextLeftIdx = (tempIdx + 1) * 2 - 1
            nextRightIdx = (tempIdx + 1) * 2
            if nextLeftIdx >= len(heapArr):
                return
            elif nextRightIdx >= len(heapArr):
                if heapArr[nextLeftIdx] > lastValue:
                    heapArr[tempIdx] = heapArr[nextLeftIdx]
                    heapArr[nextLeftIdx] = lastValue
            elif heapArr[nextLeftIdx] > heapArr[nextRightIdx] and lastValue < heapArr[nextLeftIdx]:
                heapArr[tempIdx] = heapArr[nextLeftIdx]
                heapArr[nextLeftIdx] = lastValue
                tempIdx = nextLeftIdx
                sinkDown()
            elif heapArr[nextLeftIdx] < heapArr[nextRightIdx] and lastValue < heapArr[nextRightIdx]:
                heapArr[tempIdx] = heapArr[nextRightIdx]
                heapArr[nextRightIdx] = lastValue
                tempIdx = nextRightIdx
                sinkDown()
            else:
                return
        sinkDown()
        return maxValue, heapArr
        
    
MBH = MaxBinaryHeap()
print(MBH.insert(41))
print(MBH.insert(39))
print(MBH.insert(33))
print(MBH.insert(18))
print(MBH.insert(27))
print(MBH.insert(12))
print(MBH.insert(55))
print(MBH.extractMax())
print(MBH.extractMax())
print(MBH.extractMax())
print(MBH.extractMax())
print(MBH.extractMax())
print(MBH.extractMax())
print(MBH.extractMax())
print(MBH.extractMax())
print(MBH.extractMax())
