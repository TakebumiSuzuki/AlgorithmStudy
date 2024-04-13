def factorial(num):
    result = 1;
    def helper(x):
        if x == 0:
            return
        nonlocal result;
        result *= x
        helper(x-1)
    
    helper(num);
    return result

print(factorial(1))