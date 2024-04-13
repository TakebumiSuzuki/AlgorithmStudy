def quickSort(arr, leftIdx = 0, rightIdx = -10):
    if rightIdx == -10: 
        rightIdx = len(arr) - 1
    if leftIdx >= rightIdx: 
        return
    pivotIdx = leftIdx
    first = arr[pivotIdx]
    for i in range(leftIdx + 1, rightIdx + 1):
        if first >= arr[i]:
            pivotIdx += 1
            swap(arr, i, pivotIdx)
    swap(arr, pivotIdx, leftIdx)
    
    quickSort(arr, leftIdx, pivotIdx - 1) #pivotが左端の場合、つまりpivotIdxが0の時、ここが-1になり、leftIdx>rightIdxになるケースがある
    quickSort(arr, pivotIdx + 1, rightIdx)#pivotが右端の場合、ここが+1になり、leftIdx>rightIdxになるケースがある


def swap(arr, idx1, idx2):
    temp = arr[idx2]
    arr[idx2] = arr[idx1]
    arr[idx1] = temp


arr = [10, -201, 3, 6, 8, 10, 1, 2, 1, -100, -100]
quickSort(arr)
print(arr)