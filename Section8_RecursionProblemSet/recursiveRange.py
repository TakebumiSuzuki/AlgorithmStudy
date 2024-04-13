def recursiveRange(num):
    result = 0
    def helper(someNum):
        if someNum == 0:
            return;
        nonlocal result;
        nonlocal num;
        result += someNum
        if someNum > 0:
            helper(someNum - 1)
        elif someNum < 0:
            helper(someNum + 1)
        
    helper(num);
    return result;

print(recursiveRange(10))
    