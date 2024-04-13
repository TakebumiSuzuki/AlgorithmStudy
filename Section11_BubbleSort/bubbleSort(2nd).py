def bubbleSort(arr):
    for i in range(len(arr) - 1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    
    return arr

print(bubbleSort([3,5,1,7,2,10,-1,6,4,3,-5]))