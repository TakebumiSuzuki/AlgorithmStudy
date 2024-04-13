def insertionSort(arr): #ビデオの中での方法の方が多少綺麗
    for i in range(1, len(arr)):
        temp = arr[i]
        for j in range(i-1, -1, -1):
            arr[j+1] = arr[j]
            if arr[j] <= temp:
                arr[j+1] = temp
                break
            if j == 0:
                arr[j] = temp
    return arr


print(insertionSort([2,-10,1,12,3,100,-3,-1,4,2,6,0,1,3, -30, 1000]))          