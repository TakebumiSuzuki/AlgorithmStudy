def productOfArray(arr):
    if len(arr) == 0: return 1 #if not arr: return 1 という書き方もある
    last = arr.pop()
    return last * productOfArray(arr)

print(productOfArray([3,3,3,2,1]))
