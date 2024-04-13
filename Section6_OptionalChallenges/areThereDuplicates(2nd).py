def areThereDuplicates(*args):
    dic = {}
    for ele in args:
        dic[ele] = dic.get(ele, 0) + 1
        if dic[ele] == 2:
            return True
    return False

print(areThereDuplicates(1, 2, 3)) #false
print(areThereDuplicates(1, 2, 2)) #true 
print(areThereDuplicates('a', 'b', 'c', 'a') ) #true