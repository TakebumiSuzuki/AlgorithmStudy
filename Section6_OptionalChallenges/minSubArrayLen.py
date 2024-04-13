def minSubArrayLen(arr, num):
    minimumValue = 0
    for winSize in range(len(arr)):
        firstSum = 0;
        for i in range(winSize):
            firstSum += arr[i];
        
        maxValue = firstSum;
        tempValue = firstSum;
        
        for i in range(len(arr) - winSize):
            tempValue = tempValue + arr[i + winSize] - arr[i];
            maxValue = tempValue if tempValue > maxValue else maxValue;
        
        if maxValue >= num:
            minimumValue = winSize;
            break;
        
    return minimumValue;
        
        
print(minSubArrayLen([1,4,16,22,5,7,8,9,10],95));
