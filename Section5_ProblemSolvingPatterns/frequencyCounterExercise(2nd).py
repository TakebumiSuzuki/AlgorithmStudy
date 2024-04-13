def validAnagram(str1, str2):
    if len(str1) != len(str2): return False
    dic = {}
    for char in str1:
        dic[char] = dic.get(char, 0) + 1
    for char in str2:
        value = dic.get(char, 0)
        if value == 0: return False
        dic[char] -= 1
    return True

print(validAnagram('awesome', 'awesom'))# false
print(validAnagram('amanaplanacanalpanama', 'acanalmanplanpamana'))# false
print(validAnagram('qwerty', 'qeywrt'))# true
print(validAnagram('texttwisttime', 'timetwisttext'))# true

    
    