def areThereDuplicates(*args):
    sortedList = sorted(args);
    for i in range(len(sortedList) - 1):
        if sortedList[i] == sortedList[i+1]:
            return True
    return False

x = areThereDuplicates(2,5,6,12,1,67,100,4)
print(x)