def isPalindrome(str):
    if len(str) == 0: return True
    first = str[0]
    last = str[-1]
    if first != last: 
        return False
    else:
        return isPalindrome(str[1:-1])
        
print(isPalindrome("tacocat"))