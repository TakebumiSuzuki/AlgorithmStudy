def findRotatedIndex(arr, num):
    if arr is None: return -1
    if len(arr) == 1:
        if arr[0] == num: return 1
        else: return -1
    notchIdx = findNotchIdx(arr, num)
    last = arr[len(arr) - 1]
    if num > last:
        return findNumber(arr[:notchIdx], num)

    else:
        if findNumber(arr[notchIdx:len(arr)], num) == -1: return -1
        else: return findNumber(arr[notchIdx:len(arr)], num) + notchIdx


def findNotchIdx(arr, num):
    i = 0
    j = len(arr) - 1
    last = arr[len(arr) - 1]
    
    def process(arr, i, j):
        centerIdx = (i + j) // 2
        center = arr[centerIdx]
        if center <= last:
            if centerIdx == 0:
                return 0
            if center > arr[centerIdx - 1]:
                j = centerIdx
                return process(arr, i, j)
            else:
                return centerIdx
            
        else:
            if center > arr[centerIdx + 1]:
                return centerIdx + 1
            else: 
                i = centerIdx
                return process(arr, i, j)
    
    return process(arr, i, j)


def findNumber(arr, num):
    i = 0
    j = len(arr) - 1
    def process(arr, i, j):
        centerIdx = (i + j) // 2
        center = arr[centerIdx]
        if center == num:
            return centerIdx
        if i == j :
            return -1
        if center > num:
            if j == 0: 
                return -1
            j = centerIdx
        else:
            if i == len(arr) - 1:
                return -1
            i = centerIdx + 1
            
        return process(arr, i, j)
        
    return process(arr, i, j)
        
    
    
print(findRotatedIndex([3,4,1,2],4)) # 1
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 8)) # 2
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 3)) # 6
print(findRotatedIndex([37,44,66,102,10,22],14)) # -1
print(findRotatedIndex([6, 7, 8, 9, 1, 2, 3, 4], 12)) # -1
print(findRotatedIndex([11,12,13,14,15,16,3,5,7,9], 16)) # 5