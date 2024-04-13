def maxSubarraySum(arr, num):
    if len(arr) < num:
        return None
    
    subIndex = 0;
    addIndex = num;
    
    firstSum = 0;
    for i in range(num):
        firstSum += arr[i];
    
    maxValue = firstSum;
    tempValue = firstSum;
    while addIndex < len(arr):
        tempValue = tempValue + arr[addIndex] - arr[subIndex];
        maxValue = tempValue if tempValue > maxValue else maxValue;
        subIndex += 1;
        addIndex += 1;
    
    return maxValue


print(maxSubarraySum([2,3], 3));

