def flatten(arr):
    result = []
    
    def process(arr):
        firstElem = arr[0]
        if type(firstElem) is list:
            newList = firstElem if len(arr) == 1 else firstElem + arr[1:] #extend()を使うとin placeなのでnewListはNoneになってしまう
            process(newList)
        else:
            result.append(firstElem)
            if len(arr) == 1: return
            process(arr[1:])
            
    process(arr)
    return result  


print(flatten([1, 2, 3, [4, 5] ]))  
print(flatten([1, [2, [3, 4], [[5]]]]))  
print(flatten([[1],[2],[3]]))  
print(flatten([[[[1], [[[2]]], [[[[[[[3]]]]]]]]]])) 
    