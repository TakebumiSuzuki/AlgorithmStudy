def maxSubarraySum(arr, num):
    if len(arr) < num: return None
    if len(arr) == 0: return None
    current = 0
    for i in range(num):
        current += arr[i]
    maxSum = current
    for i in range(len(arr) - num):
        current = current - arr[i] + arr[i + num]
        maxSum = max(current, maxSum)
    return maxSum
        
print(maxSubarraySum([100,200,300,400], 2)) # 700
print(maxSubarraySum([1,4,2,10,23,3,1,0,20], 4))  # 39 
print(maxSubarraySum([-3,4,0,-2,6,-1], 2)) # 5
print(maxSubarraySum([3,-2,7,-4,1,-1,4,-2,1],2)) # 5
print(maxSubarraySum([2,3], 3)) # null