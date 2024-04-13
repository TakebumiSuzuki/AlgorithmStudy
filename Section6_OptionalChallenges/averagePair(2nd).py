def averagePair(arr, ave):
    if len(arr) == 0: return False
    i = 0
    j = len(arr) - 1
    while i != j:
        if arr[i] + arr[j] > ave * 2:
            j -= 1
        elif arr[i] + arr[j] < ave * 2:
            i += 1
        else:
            return True
    return False

print(averagePair([1,2,3],2.5)) # true
print(averagePair([1,3,3,5,6,7,10,12,19],8)) # true
print(averagePair([-1,0,3,4,5,6], 4.1)) # false
print(averagePair([],4)) # false