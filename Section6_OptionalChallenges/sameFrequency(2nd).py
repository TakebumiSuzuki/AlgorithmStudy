def sameFrequency(num1, num2):
    dic = {}
    count1 = 0
    currentNum1 = num1
    while currentNum1 > 0:
        remainder = currentNum1 % 10
        dic[remainder] = dic.get(remainder, 0) + 1
        count1 += 1
        currentNum1 //= 10
    
    count2 = 0
    currentNum2 = num2
    while currentNum2 > 0:
        remainder = currentNum2 % 10
        dic[remainder] = dic.get(remainder, 0) - 1
        count2 += 1
        currentNum2 //= 10
        if dic[remainder] < 0: return False
    
    if count1 == count2: return True
    else: return False
    
print(sameFrequency(182,281)) # true
print(sameFrequency(34,14)) #false
print(sameFrequency(3589578, 5879385)) # true
print(sameFrequency(22,222)) #false
        
    