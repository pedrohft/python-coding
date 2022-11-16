def move_zeros(nums):
        l = 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1

        return nums
print(move_zeros([0,0,1,2]))