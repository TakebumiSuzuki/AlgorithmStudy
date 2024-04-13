def insertionSort(arr):#このコードは無駄が多い、(2nd)_2の方を参照。さらにビデオの中での方法が一番綺麗
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            print(arr[i+1])
            if i == 0:
                arr.insert(0, arr[1])
                del arr[2]
            else:
                for j in range(i + 1):
                    if arr[j] >= arr[i + 1]:
                        arr.insert(j, arr[i + 1])
                        del arr[i + 2]
                        break
    return arr

print(insertionSort([2,-10,1,12,3,100,-3,-1,4,2,6,0,1,3]))
        