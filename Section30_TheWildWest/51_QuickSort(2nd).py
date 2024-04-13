def quickSort(arr, comparator = None, start = 0, end = len(arr) - 1):
    if len(arr) <= 1:
        return arr
    if end is None:
        end = len(arr) - 1
    if end - start <= 0: 
        return
    pivotIdx = pivot(arr, comparator, start, end)
    quickSort(arr, comparator, start, pivotIdx - 1)
    quickSort(arr, comparator, pivotIdx + 1, end)
    
    return arr
    
    
def pivot(arr, comparator = None, start = 0, end = None):
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

def oldestToYoungest(a, b):
    return b['age'] - a['age']

def strComp(a, b):
    if a < b:
        return -1
    elif a > b: 
        return 1
    return 0;

    

nums = [4, 20, 12, 10, 7, 9]
print(quickSort(nums))  # [4, 7, 9, 10, 12, 20]

nums = [0, -10, 7, 4]
print(quickSort(nums))  # [-10, 0, 4, 7]

nums = [1, 2, 3]
print(quickSort(nums))  # [1, 2, 3]

nums = []
print(quickSort(nums))  # []

nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32]
print(quickSort(nums))  # [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]

kitties = ["LilBub", "Garfield", "Heathcliff", "Blue", "Grumpy"]
print(quickSort(kitties, strComp))  # ["Blue", "Garfield", "Grumpy", "Heathcliff", "LilBub"]

moarKittyData = [
    {"name": "LilBub", "age": 7},
    {"name": "Garfield", "age": 40},
    {"name": "Heathcliff", "age": 45},
    {"name": "Blue", "age": 1},
    {"name": "Grumpy", "age": 6}
    ]
print(quickSort(moarKittyData, oldestToYoungest))
