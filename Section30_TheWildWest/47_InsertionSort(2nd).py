def insertionSort(arr, comparator = None):
    if len(arr) <= 1: return arr
    for tempIdx in range(1, len(arr)):
        tempElem = arr[tempIdx]
        j = tempIdx - 1
        
        while j >= 0:
            result = None
            if not (hasattr(comparator, '__call__')):
                if tempElem < arr[j]: result = True  
                else: result = False  
            else:
                resultNum = comparator(tempElem, arr[j])
                if resultNum < 0: result = True 
                else: result = False
            
            if result == False:
                break
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = tempElem
        
    return arr

def strComp(a, b):
    if a < b:
        return -1
    elif a > b: 
        return 1
    return 0;

def oldestToYoungest(a, b):
    return b.age - a.age 

print(insertionSort([4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32]))
print(insertionSort(["LilBub", "Garfield", "Heathcliff", "Blue", "Grumpy", "Arther", "Zoff"], strComp))