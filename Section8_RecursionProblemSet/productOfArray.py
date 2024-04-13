def productOfArray(arr):
    result = 1;
    def helper(someArr):
        nonlocal result;
        if not someArr:
            return;
        result *= someArr[0];
        
        helper(someArr[1:])
    
    helper(arr);
    return result;


print(productOfArray([2,100,3,1,2]))