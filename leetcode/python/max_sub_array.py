def maxSubArray(nums):
    maxSum = nums[0]
    currentSum = 0

    for i in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum+=i
        maxSum = max(maxSum, currentSum)
    
    return maxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))