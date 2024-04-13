def reverse(str):
    newStr = ""
    def process(str):
        if len(str) == 0: return
        last = str[-1]
        str = str[:-1]
        nonlocal newStr
        newStr += last
        process(str)
    process(str)
        
    return newStr


print(reverse("opppppo"))