def someRecursive(arr, func):
    if len(arr) == 0 : return False
    last = arr.pop()
    if func(last) == True:
        return True
    
    return someRecursive(arr, func)


print(someRecursive([1,5,11,9,3,9],lambda x: x % 2 == 0))