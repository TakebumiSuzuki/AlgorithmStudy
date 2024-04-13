def selectionSort(arr):
    for i in range(len(arr)):
        tempMinVal = arr[i]
        tempMinIdx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < tempMinVal:
                tempMinVal = arr[j]
                tempMinIdx = j
        temp = arr[tempMinIdx]
        arr[tempMinIdx] = arr[i]
        arr[i] = temp
    return arr

print(selectionSort([2, 2,5,4, 6, 25, 2, 111, 8,2,4,1,-3, -100]))