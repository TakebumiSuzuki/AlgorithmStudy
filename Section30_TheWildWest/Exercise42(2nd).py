def sortedFrequency(arr, num):
    if arr is None: return 0
    if len(arr) == 1:
        if arr[0] == num: return 1
        if arr[0] != num: return 0
    leftIdx = findLeftIdx(arr, num)
    rightIdx = findRightIdx(arr, num)
    # print(rightIdx)
    # print(leftIdx)
    if leftIdx is not None and rightIdx is not None:
        return rightIdx - leftIdx + 1
    else: return -1


def findLeftIdx(arr, num):
    i = 0
    j = len(arr) - 1
    
    while i < j:
        midIdx = (i + j) // 2
        midVal = arr[midIdx]
        if midVal < num and arr[midIdx + 1] == num:
            return midIdx + 1
        if midVal < num and arr[midIdx + 1] > num:
            return None
        elif midVal >= num:
            j = midIdx
        else:
            i = midIdx + 1
    if j == 0 and arr[j] == num:
        return 0
    else:
        return None

def findRightIdx(arr, num):
    i = 0
    j = len(arr) - 1
    
    while i < j:
        midIdx = (i + j) // 2
        midVal = arr[midIdx]
        if midVal == num and arr[midIdx + 1] > num:
            return midIdx
        elif midVal > num:
            j = midIdx
        else:
            i = midIdx + 1
    if j == 0: return None
    if i == len(arr) - 1:
        if arr[i] == num: return i
        else: return None
    return None


# print(sortedFrequency([1,1,2,2,2,2,3],2)) # 4 
# print(sortedFrequency([1,1,2,2,2,2,3],3)) # 1 
# print(sortedFrequency([1,1,2,2,2,2,3],1)) # 2 
# print(sortedFrequency([1,1,2,2,2,2,3],4)) # -1
print(sortedFrequency([1,1,2,2,2,2,3,4,6,6,6,9,12,15,17,17,17,17,17,100,100,100],99))