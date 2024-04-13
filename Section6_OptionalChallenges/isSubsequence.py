def isSubsequence(char1, char2):
    len1 = len(char1);
    len2 = len(char2);
    if len1 > len2:
        return False;
    i = 0;
    j = 0;
    
    while True:
        if char1[i] != char2[j]: #マッチしなかった時
            j += 1;
            if j == len2:
                return False;
        else: #マッチした時
            i += 1;
            j += 1;
            if i == len1:
                return True;
            if j == len2:
                return False
            
        
print(isSubsequence('abc', 'acb'));        
    