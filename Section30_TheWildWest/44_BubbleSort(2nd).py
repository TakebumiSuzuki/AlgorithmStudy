def bubbleSort(arr, comparator = None):
    if len(arr) <= 1: return arr
    for i in range(len(arr) - 1):
        swapped = False
        for j in range(0, len(arr) - i - 1):
            result = False
            if not (hasattr(comparator, '__call__')):
                result = arr[j] > arr[j + 1]
            else:
                resultNum = comparator(arr[j], arr[j + 1])
                if resultNum > 0: result = True
                else: result = False
                
            if result:
                swap(arr, j, j + 1)
                swapped = True
        if swapped == False:
            break
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


print(bubbleSort([4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32]))
print(bubbleSort(["LilBub", "Garfield", "Heathcliff", "Blue", "Grumpy"], strComp))       
    