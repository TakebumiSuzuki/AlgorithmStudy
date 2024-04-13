def countZeroes(arr):
    i = 0
    j = len(arr) - 1
    
    while i < j:
        midIdx = (i + j) // 2
        midVal =  arr[midIdx]
        if midVal == 1 and arr[midIdx + 1] == 0:
            return len(arr) - midIdx - 1 
        if midVal == 1:
            i = midIdx + 1
        if midVal == 0:
            j = midIdx
    
    if j == 0:
        return len(arr)
    if i == len(arr) - 1:
        return 0
            
print(countZeroes([1,1,1,1,0,0])) # 2
print(countZeroes([1,0,0,0,0])) # 4
print(countZeroes([0,0,0])) # 3
print(countZeroes([1,1,1,1])) # 0

            
    
        
     