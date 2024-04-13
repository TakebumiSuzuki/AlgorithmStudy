def power(base, exponent):
    result = 1;
    
    def helper(base, exponent):
        if exponent == 0:
            return
        nonlocal result
        result *= base
        helper(base, exponent - 1);
    
    helper(base, exponent)
    return result


y = power(5,1)
print(y)



