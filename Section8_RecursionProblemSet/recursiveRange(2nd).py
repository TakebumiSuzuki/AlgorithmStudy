def recursiveRange(num):
    if num == 0: return 0
    elif num > 0:
        return recursiveRange(num - 1) + num
    else:
        return recursiveRange(num + 1) + num

print(recursiveRange(0))