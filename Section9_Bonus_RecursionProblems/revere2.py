def reverse(str):
    if len(str) == 0:
        return ""
    
    char = str[-1]
    return char + reverse(str[:-1])

print(reverse("takebumi Suzuki"))