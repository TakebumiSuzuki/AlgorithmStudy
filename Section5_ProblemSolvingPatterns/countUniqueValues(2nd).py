def countUniqueValues(arr):
    if len(arr) == 0: return 0
    prevIdx = 0
    currentIdx = 0
    counter = 1
    
    while currentIdx < len(arr):
        if arr[prevIdx] != arr[currentIdx]:
            counter += 1
            prevIdx = currentIdx
        currentIdx += 1
        
    return counter


    