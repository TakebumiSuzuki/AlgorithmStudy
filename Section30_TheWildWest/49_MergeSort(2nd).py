def mergeSort(arr, comparator = None):
    if len(arr) <= 1: return arr
    
    centerIdx = (len(arr)) // 2
    
    left = mergeSort(arr[:centerIdx], comparator)
    right = mergeSort(arr[centerIdx:], comparator)
    
    return merge(left, right, comparator)


def merge(arr1, arr2, comparator = None):
    i = 0
    j = 0
    resultArr = []
    
    while i < len(arr1) and j < len(arr2):
        result = None
        if not (hasattr(comparator, '__call__')):
            if arr1[i] >= arr2[j]: result = True  
            else: result = False  
        else:
            resultNum = comparator(arr1[i], arr2[j])
            if resultNum > 0: result = True 
            else: result = False
        
        
        if result:
            resultArr.append(arr2[j])
            j += 1
        else:
            resultArr.append(arr1[i])
            i += 1
    
    if i == len(arr1):
        for k in range(j, len(arr2)):
            resultArr.append(arr2[k])
    if j == len(arr2):
        for k in range(i, len(arr1)):
            resultArr.append(arr1[k])
    
    return resultArr

def strComp(a, b):
    if a < b:
        return -1
    elif a > b: 
        return 1
    return 0;

def oldestToYoungest(a, b):
    return b["age"] - a["age"] 

nums = [4, 20, 12, 10, 7, 9]
print(mergeSort(nums))  # [4, 7, 9, 10, 12, 20]

nums = [0, -10, 7, 4]
print(mergeSort(nums))  # [-10, 0, 4, 7]

nums = [1, 2, 3]
print(mergeSort(nums))  # [1, 2, 3]

nums = []
print(mergeSort(nums))  # []

nums = [4, 3, 5, 3, 43, 232, 4, 34, 232, 32, 4, 35, 34, 23, 2, 453, 546, 75, 67, 4342, 32]
print(mergeSort(nums))  # [2, 3, 3, 4, 4, 4, 5, 23, 32, 32, 34, 34, 35, 43, 67, 75, 232, 232, 453, 546, 4342]

kitties = ["LilBub", "Garfield", "Heathcliff", "Blue", "Grumpy"]
print(mergeSort(kitties, strComp))  # ["Blue", "Garfield", "Grumpy", "Heathcliff", "LilBub"]

moar_kitty_data = [
    {"name": "LilBub", "age": 7},
    {"name": "Garfield", "age": 40},
    {"name": "Heathcliff", "age": 45},
    {"name": "Blue", "age": 1},
    {"name": "Grumpy", "age": 6}
]

print(mergeSort(moar_kitty_data, oldestToYoungest))



