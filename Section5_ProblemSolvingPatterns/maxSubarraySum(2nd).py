def maxSubarraySum(arr, num):
    if len(arr) == 0: return None
    if len(arr) < num: return None
    
    maxNum = 0
    cumulativeDiff = 0
    for i in range(len(arr) - num):
        diff = arr[i + num] - arr[i]
        cumulativeDiff += diff
        maxNum = max(maxNum, cumulativeDiff)
    
    base = 0
    for i in range(num):
        base += arr[i]
    
    return base + maxNum

print(maxSubarraySum([4,2,1,6,2],4))
    
    
