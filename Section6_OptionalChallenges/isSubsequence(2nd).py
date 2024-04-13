def isSubsequence(char1, char2):
    i = 0
    j = 0
    while i < len(char1) and j < len(char2):
        text1 = char1[i]
        text2 = char2[j]
        if text1 == text2:
            if i == len(char1) - 1: return True
            i += 1
        j += 1
    
    return False

print(isSubsequence('hello', 'hello world')); # true
print(isSubsequence('sing', 'sting')); # true
print(isSubsequence('abc', 'abracadabra')); # true
print(isSubsequence('abc', 'acb')); # false 

        
            