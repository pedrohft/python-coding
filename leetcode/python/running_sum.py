def runningSum(nums):
    for i in range(len(nums)-1):
        print(nums[i], nums[i+1])
        nums[i], nums[i+1] = nums[i], nums[i] + nums[i+1]
    return nums

runningSum([1,2,3,4])