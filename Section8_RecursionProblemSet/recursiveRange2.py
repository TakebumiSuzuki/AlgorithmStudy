def recursiveRange(num):
    if num == 0:
        return 0;
    if num > 0:
        return num + recursiveRange(num - 1);
    elif num < 0:
        return num + recursiveRange(num + 1);
    
    
print(recursiveRange(-3))