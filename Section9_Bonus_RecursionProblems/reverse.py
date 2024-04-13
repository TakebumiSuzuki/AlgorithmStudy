def reverse(str):
    result = "";
    
    def helper(strings):
        nonlocal result;
        if len(strings) == 0:
            return;
        result += strings[-1];
        helper(strings[:-1]);

    helper(str);
    return result;

print(reverse("1jife3"))