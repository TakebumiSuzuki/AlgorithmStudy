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


print(mostDigits([1, 9, 10, 100, 99])); # 3
print(mostDigits([100, 1010, 1, 500])); # 4
print(mostDigits([0, 100000, 400, 12, 8])); # 6
print(mostDigits([])); # 0