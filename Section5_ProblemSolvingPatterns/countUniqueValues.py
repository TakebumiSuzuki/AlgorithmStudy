
def contUniqueValue(arr):
    newArr = [];
    oldValue = 0
    for i in arr:
            
        if i != oldValue:
            newArr.append(i)
        else:
            continue;
        
        oldValue = i;
    
    return len(newArr);
        
    
y = contUniqueValue([1,2,3,4,4,4,7,7,12,12,13]) 
print(y)
   


