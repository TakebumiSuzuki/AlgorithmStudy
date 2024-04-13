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


arr1 = [1, 3, 4, 5]
arr2 = [2, 4, 6, 8]

print(merge(arr1, arr2))  # [1, 2, 3, 4, 4, 5, 6, 8]
print(arr1)  # [1, 3, 4, 5]
print(arr2)  # [2, 4, 6, 8]

arr3 = [-2, -1, 0, 4, 5, 6]
arr4 = [-3, -2, -1, 2, 3, 5, 7, 8]

print(merge(arr3, arr4))  # [-3, -2, -2, -1, -1, 0, 2, 3, 4, 5, 5, 6, 7, 8]

arr5 = [3, 4, 5]
arr6 = [1, 2]

print(merge(arr5, arr6))  # [1, 2, 3, 4, 5]

names = ["Bob", "Ethel", "Christine"]
otherNames = ["M", "Colt", "Allison", "SuperLongNameOMG"]

def stringLengthComparator(str1, str2):
    return len(str1) - len(str2)

print(merge(names, otherNames, stringLengthComparator))  # ["M", "Bob", "Colt", "Ethel", "Allison", "Christine", "SuperLongNameOMG"]



