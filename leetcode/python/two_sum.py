# class Solution:
#     def twoSum(nums, target):
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 print(i,j)
#                 if ((nums[i] + nums[j]) == target) and i!=j:
#                     return i, j

#         return -1

# print(Solution.twoSum([3,2,4], 6))


class Solution:
    def twoSum(nums, target):
        hashMap={}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap:
                return [hashMap[diff], i]
            hashMap[n] = i
        return 
           

print(Solution.twoSum([1,2,4,4], 8))