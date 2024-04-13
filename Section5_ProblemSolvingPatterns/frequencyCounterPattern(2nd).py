def same(arr1, arr2):
    if len(arr1) != len(arr2): return False
    
    dic = {}
    for ele in arr1:
        if ele ** 2 in dic:
            dic[ele ** 2] += 1
        else:
            dic[ele ** 2] = 1
    for ele in arr2:
        if (ele not in dic or dic[ele] == 0):
            return False
        dic[ele] -= 1
    return True
        

print(same([2,4,6,1, 4], [1, 16,4,36,25]))

    
    
    