def maxSubarraySum(arr, winSize):
    if len(arr) < winSize:
        return None
    
    firstSum = 0;
    for i in range(winSize):
        firstSum += arr[i];
    
    maxValue = firstSum;
    tempValue = firstSum;
    for i in range(len(arr) - winSize):
        tempValue = tempValue + arr[i + winSize] - arr[i];
        maxValue = tempValue if tempValue > maxValue else maxValue;
    
    return maxValue;

print(maxSubarraySum([-3,4,0,-2,6,-1], 2));