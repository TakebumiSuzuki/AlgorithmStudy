
def maxSubarraySum(arr, num):
    if len(arr) <= num:
        return 0;
    
    maxIndex = len(arr) - num;
    cumulative = 0;
    max_cumu = 0;
    for i in range(maxIndex):
        add = arr[i + num];
        sub = arr[i];
        diff = add - sub;
        cumulative += diff;
        if max_cumu < cumulative:
            max_cumu = cumulative;
    baseSum = 0;
    for i in range(num):
        baseSum += arr[i];
    return baseSum + max_cumu;

y = maxSubarraySum([2,3], 4);
print(y);
        
        

        