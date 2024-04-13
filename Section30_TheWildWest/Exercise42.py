def sortedFrequency(arr, num):
    if getRightIdx(arr, num) == None or getLeftIdx(arr, num) == None: return None
    return getRightIdx(arr, num) - getLeftIdx(arr, num) + 1


def getLeftIdx(arr, num):
    i = 0
    j = len(arr) - 1
    
    while True:
        centerIdx = (i + j) // 2
        center = arr[centerIdx]
        
        if center == num:
            if centerIdx == 0:
                return 0
            if arr[centerIdx - 1] == num:
                j = centerIdx
            else:
                return centerIdx
        
        elif center > num:
            if j == 0:
                return None
            j = centerIdx
            
        else: #center < num 
            if i == len(arr) - 1:
                return None
            i = centerIdx + 1
            
            
def getRightIdx(arr, num):
    i = 0
    j = len(arr) - 1
    
    while True:
        centerIdx = (i + j) // 2
        center = arr[centerIdx]
        
        if center == num:
            if centerIdx == len(arr) - 1:
                return centerIdx
            if arr[centerIdx + 1] == num:
                i = centerIdx + 1
            else:
                return centerIdx
        
        elif center > num:
            if j == 0:
                return None
            j = centerIdx
            
        else: #center < num 
            if i == len(arr) - 1:
                return None
            i = centerIdx + 1
            
    
    
print(sortedFrequency([1,1,2,2,2,2,3],2)) # 4 
print(sortedFrequency([1,1,2,2,2,2,3],3)) # 1 
print(sortedFrequency([1,1,2,2,2,2,3],1)) # 2 
print(sortedFrequency([1,1,2,2,2,2,3],4)) # -1