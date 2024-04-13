def mergeSort(arr): #ビデオのコードの方がシンプル
    if len(arr) <= 1: return arr
    halfIdx = len(arr) // 2
    left = arr[:halfIdx]
    right = arr[halfIdx:]
    if len(left) == 1 and len(right) == 1:
        return merge(left, right)
    else:
        return merge(mergeSort(left), mergeSort(right))

def merge(arr1, arr2):
    i = 0
    j = 0
    resultArr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            resultArr.append(arr1[i])
            i += 1
        elif arr1[i] > arr2[j]:
            resultArr.append(arr2[j])
            j += 1
    if i >= len(arr1):
        resultArr += arr2[j:]
    if j >= len(arr2):
        resultArr += arr1[i:]
    return resultArr


print(mergeSort([13,5,1,-2,5,0,-100,4,7,10,-19]))