def selectionSort(arr, comparator = None):
    if len(arr) <= 1: return arr
    for i in range(len(arr) - 1):
        firstElem = arr[i]
        smallestElem = firstElem
        smallestIdx = i
        for j in range(i + 1, len(arr)):
            if not (hasattr(comparator, '__call__')):
                if smallestElem > arr[j]:
                    smallestElem = arr[j]
                    smallestIdx = j
            else:
                resultNum = comparator(smallestElem, arr[j])
                if resultNum > 0:
                    smallestElem = arr[j]
                    smallestIdx = j
        if firstElem != smallestElem:
            swap(arr, i, smallestIdx)
        
    return arr
    
def swap(arr, i, j):
    temp = arr[j]
    arr[j] = arr[i]
    arr[i] = temp
    
def strComp(a, b):
    if a < b:
        return -1
    elif a > b: 
        return 1
    return 0;

def oldestToYoungest(a, b):
    return b.age - a.age


print(selectionSort([4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32]))
print(selectionSort(["LilBub", "Garfield", "Heathcliff", "Blue", "Grumpy"], strComp))  