def countZeroes(arr):
    i = 0
    j = len(arr) - 1
    if arr == [0]: return 1
    if arr == [1]: return 0
    
    while True :
        centerIdx = (i + j) // 2
        
        if arr[centerIdx] == 1 and arr[centerIdx + 1] == 0:
            return len(arr) - centerIdx - 1
        elif arr[centerIdx] == 0:
            j = centerIdx
        else:
            i = centerIdx + 1
            
        if i == len(arr) - 1:
            return 0
        if j == 0 and arr[0] == 0:
            return len(arr)
            
print(countZeroes([1,1,1,1,0,0])) # 2
print(countZeroes([1,0,0,0,0])) # 4
print(countZeroes([0,0,0])) # 3
print(countZeroes([1,1,1,1])) # 0