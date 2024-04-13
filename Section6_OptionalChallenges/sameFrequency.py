def samefrequency(num1, num2):
    digitBag = {};
    digitCount = 0
    
    moreThanOneDigit1 = True;
    tempNum1 = num1
    digit = 0
    while moreThanOneDigit1:
        oneTenth = tempNum1 // 10;
        if 1 <= tempNum1 < 10:
            digit = tempNum1;
            moreThanOneDigit1 = False;
        else:
            digit = tempNum1 - (oneTenth * 10);
            tempNum1 = oneTenth;
        
        digitBag[digit] = 1 if digit not in digitBag else digitBag[digit] + 1;
        digitCount += 1
        
    
    moreThanOneDigit2 = True;
    tempNum2 = num2;
    while moreThanOneDigit2:
        oneTenth = tempNum2 // 10;
        if 1 <= tempNum2 < 10:
            digit = tempNum2;
            moreThanOneDigit2 = False;
        else:
            digit = tempNum2 - (oneTenth * 10);
            tempNum2 = oneTenth;
            
        if digit not in digitBag or digitBag[digit] == 0:
            return False;
        else:
            digitBag[digit] -= 1;
        digitCount -= 1
    
    if digitCount == 0:
        return True;
    else:
        return False
    


y = samefrequency(22212, 12222);
print(y);
