def bubbleSort(arr):
    for i in range(len(arr) -1, -1, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;

    return arr    
    
print(bubbleSort([9,1,7,12, -3, -22, 18,2,2,5,3,4]))