def radixSort(arr):
    maxDigit = mostDigits(arr)
    currentArr = arr
    
    for i in range(maxDigit):
        buckets = [[] for _ in range(10)]
        for num in currentArr:
            digitNum = getDigit(num, i)
            buckets[digitNum].append(num)
        sortedArr = []
        for numSet in buckets:
            sortedArr.extend(numSet)
            currentArr = sortedArr
    return currentArr
    
    

def getDigit(num, i):
    return num // (10 ** i) % 10

def mostDigits(arr):
    maxDigit = 0
    for num in arr:
        k = digitCount(num)
        maxDigit = max(maxDigit, k)
    return maxDigit
    
def digitCount(num):
    i = 1
    while True:
        num = num // 10
        if num < 1:
            break
        i += 1
    return i

print(radixSort([8, 6, 1, 12])); # [1, 6, 8, 12]
print(radixSort([10, 100, 1, 1000, 10000000])); # [1, 10, 100, 1000, 10000000]
print(radixSort([902, 4, 7, 408, 29, 9637, 1556, 3556, 8157, 4386, 86, 593])); # [4, 7, 29, 86, 408, 593, 902, 1556, 3556, 4386, 8157, 9637]