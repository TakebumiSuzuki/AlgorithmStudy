def sameFrequency(num1, num2):
    digitBag = {};
    digitCount = 0;
    
    repeat1 = True;
    tempNum1 = num1;
    while repeat1:
        digit = tempNum1 % 10;
        digitBag[digit] = 1 if digit not in digitBag else digitBag[digit] + 1;
        
        tempNum1 //= 10;
        digitCount += 1;
        repeat1 = False if tempNum1 == 0 else True;
    
    repeat2 = True;
    tempNum2 = num2;
    print(digitBag)
    
    while repeat2:
        digit = tempNum2 % 10;
        if digit not in digitBag or digitBag[digit] == 0:
            return False;
        else:
            digitBag[digit] -= 1
        
        tempNum2 //= 10;
        digitCount -= 1;
        repeat2 = False if tempNum2 == 0 else True;
        
    print(digitBag)
    if digitCount == 0:
        return True
    else:
        return False
        
        
print(sameFrequency(36936111, 13619316));    
    
        