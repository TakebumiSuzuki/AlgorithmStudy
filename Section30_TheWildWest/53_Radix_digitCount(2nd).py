def digitCount(num):
    i = 1
    while True:
        num = num // 10
        if num < 1:
            break
        i += 1
    return i

print(digitCount(1)); # 1
print(digitCount(9)); # 1
print(digitCount(25)); # 2
print(digitCount(314)); # 3
print(digitCount(1234)); # 4
print(digitCount(77777)); # 5