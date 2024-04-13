def selectionSort(arr):
    for i in range(len(arr)):
        tempValue = arr[i];
        tempIndex = i;
        
        for j in range(i + 1, len(arr)):
            if arr[j] < tempValue:
                tempValue = arr[j];
                tempIndex = j;
        
        if i != tempIndex: 
            temp = arr[i];
            arr[i] = tempValue;
            arr[tempIndex] = temp;
    return arr;

print(selectionSort([2, 2,5,4, 6, 25, 2, 111, 8,2,4,1]))

        
                