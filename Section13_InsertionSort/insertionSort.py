def insertionSort(arr):
    for i in range(1,len(arr)):
        j = i
        while j >= 0:
            if j > 0 and arr[j - 1] > arr[i]:
                j -= 1;
            else:
                temp = arr[i];
                arr.pop(i);
                arr.insert(j,temp);
                break;
    return arr

print(insertionSort([2,-10,1,12,3,100,-3,-1,4,2,6,0,1,3]))                
            