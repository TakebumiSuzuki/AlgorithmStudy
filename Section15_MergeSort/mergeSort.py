def mergeSort(arr):
    dividedArr = [];
    for element in arr:
        dividedArr.append([element]);
        
    resultArr = dividedArr;
    
    while len(resultArr) > 1:
        arrPairs = len(resultArr) // 2;
        remainder = len(resultArr) % 2;
        newArr = []
        for i in range(arrPairs):
            newArr.append(combineTwoArr(resultArr[2 * i], resultArr[2 * i + 1])); 
        if remainder == 1:
                newArr.append(resultArr[-1])
        
        resultArr = newArr
        print(resultArr)
        
    return resultArr[0]
            

def combineTwoArr(arr1, arr2):
    i = 0;
    j = 0;
    newArr = [];
    
    while True:
        if arr1[i] <= arr2[j]:
            newArr.append(arr1[i]);
            i += 1;
        else:
            newArr.append(arr2[j]);
            j += 1;
            
        if i == len(arr1):
            for m in range(j, len(arr2)):
                newArr.append(arr2[m]);
            return newArr;
        elif j == len(arr2):
            for m in range(i, len(arr1)):
                newArr.append(arr1[m]);
            return newArr;
    
    
print(mergeSort([3,1,-2,5,0,-100,4,7,10,-19]))
