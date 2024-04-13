def redixSort(arr, j = 1):
    digitBag = [[] for i in range(10)];
    
    for num in arr:
        digit = num % (10 ** j) // (10 ** (j - 1));
        digitBag[digit].append(num);
        
    if j == 7:
        print(digitBag)
    
    if len(arr) == len(digitBag[0]) and max(digitBag[0]) < 10 ** j:
        return arr;
    
    sortedArr = [];
    for eleArr in digitBag:
        sortedArr += eleArr;
        
    return redixSort(sortedArr, j + 1);
    
    

print(redixSort([1174, 100000000,6,3,56,2,445,887356,6752,96824,345,3,0]))