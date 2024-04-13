def getDigit(num, i):
    return num // (10 ** i) % 10


print(getDigit(12345, 0)); # 5
print(getDigit(12345, 1)); # 4
print(getDigit(12345, 2)); # 3
print(getDigit(12345, 3)); # 2
print(getDigit(12345, 4)); # 1
print(getDigit(12345, 5)); # 0
 
print(getDigit(8987, 0)); # 7
print(getDigit(8987, 1)); # 8
print(getDigit(8987, 2)); # 9
print(getDigit(8987, 3)); # 8
print(getDigit(8987, 4)); # 0