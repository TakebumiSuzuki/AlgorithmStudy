def productOfArray(arr):
    if not arr: return 1
    num = arr[0]
    return num * productOfArray(arr[1:])

print(productOfArray([]))