def strAnagrams(str1, str2):
    
    if len(str1) != len(str2):
        return False
    
    char_count = {}
    
    for char in str1:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    for char in str2:
        if char not in char_count or char_count[char] == 0:
            return False
        else:
            char_count[char] -= 1
            
    return True

print(strAnagrams("abcdefg", "cabdgfe"))


