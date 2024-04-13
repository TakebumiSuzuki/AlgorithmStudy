def averagePair(arr, ave):
    i = 0;
    j = len(arr) - 1;
    if j < 1:
        return False
    
    while arr[i] + arr[j] != ave * 2 :
        if arr[i] + arr[j] > ave * 2:
            j -= 1;
        else:
            i += 1;
        if i == j:
            return False;
    
    return True

print(averagePair([1,2,3,4,5,6,10,11],7))