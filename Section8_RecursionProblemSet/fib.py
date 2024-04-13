def fib(repeat):
    if repeat == 1 or repeat ==2:
        return 1
    result = 0;
    
    def helper(newNum, oldNum):
        nonlocal result;
        nonlocal repeat;
        if repeat == 2:
            return
        result = newNum + oldNum;
        repeat -= 1
        helper(result, newNum);
        
    helper(1,1)
    return result;

print(fib(10))