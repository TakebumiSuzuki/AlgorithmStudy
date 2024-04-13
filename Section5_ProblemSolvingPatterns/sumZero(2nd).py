def sumZero(arr):
    if len(arr) < 2: return None
    leftIdx = 0
    rightIdx = len(arr) - 1
    
    while (arr[leftIdx] < 0 and arr[rightIdx] > 0)  :
        print(leftIdx, rightIdx)
        sum = arr[leftIdx] + arr[rightIdx]
        if sum > 0:
            rightIdx -= 1
        elif sum < 0:
            leftIdx += 1
        else:
            return (arr[leftIdx], arr[rightIdx])
        
    return None

print(sumZero([-4,-2,-1,0,1, 10, 15,20,1000, 2000]))