def areThereDuplicates(*args):
    dic = {}
    for i in args:
        if i not in dic:
            dic[i] = 1;
        else:
            return True;
        
    return False;
    




print(areThereDuplicates(3,4,3.14,6,"TEST",7,1,2,99,100,3.14));

    
    