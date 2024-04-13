def linearSearch(arr, num):
    for i in range(len(arr)):
        if num == arr[i]:
            return i;
    return -1;

print(linearSearch([10, 15, 20, 25, 30], 15))