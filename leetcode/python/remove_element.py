def removeElement(nums, val):
    count = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[count] = nums[i]
            count+=1
    return count    

print(removeElement([3,2,2,3], 3))