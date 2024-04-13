def pivot(arr, comparator = None, start =0, end = -1):
    if len(arr) <= 1: 
        return arr
    if end == -1:
        end = len(arr) - 1
    
    pivotValue = arr[start]
    swapPointIdx = start + 1
    for tempIdx in range(start + 1, end + 1):
        result = False
        if not (hasattr(comparator, '__call__')):
            if pivotValue > arr[tempIdx]:
                result = True 
        else:
            resultNum = comparator(pivotValue, arr[tempIdx])
            if resultNum > 0: result = True 
        
        if result:
            swap(arr, tempIdx, swapPointIdx)
            swapPointIdx += 1
            
    swap(arr, start, swapPointIdx - 1)
    return swapPointIdx - 1


def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp
    

arr1 = [5, 4, 9, 10, 2, 20, 8, 7, 3]
arr2 = [8, 4, 2, 5, 0, 10, 11, 12, 13, 16]
arr3 = ["LilBub", "Garfield", "Heathcliff", "Blue", "Grumpy"]

def strLength(a, b):
    return len(a) - len(b)

print(pivot(arr1))  # 3
print(pivot(arr2))  # 4
print(pivot(arr3, strLength))  # 1
print(arr3)

arr1_part1 = sorted(arr1[:3])
arr1_part2 = sorted(arr1[3:])
print(arr1_part1)  # [2, 3, 4]
print(arr1_part2)  # [5, 7, 8, 9, 10, 20]

arr2_part1 = sorted(arr2[:4])
arr2_part2 = sorted(arr2[4:])
print(arr2_part1)  # [0, 2, 4, 5]
print(arr2_part2)  # [8, 10, 11, 12, 13, 16]

arr3_part1 = sorted(arr3[:1], key=len)
arr3_part2 = sorted(arr3[1:], key=len)
print(arr3_part1)  # ["Blue"]
print(arr3_part2)  # ["LilBub", "Grumpy", "Garfield", "Heathcliff"]

    
    