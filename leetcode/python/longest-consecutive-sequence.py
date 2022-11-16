class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
            
        hight_count = 0
        l = sorted(set(nums))

        count = 0
        for i in range(len(l)-1):

            if l[i+1]-l[i] in [-1,1]:
                count+=1
            if l[i+1]-l[i] not in [-1,1]:
                count = 0
            if count > hight_count:
                hight_count = count
            
            
        return hight_count+1

#Short solution but the first runs faster;
# class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    
        nums_set = set(nums)
        longest = 0
        for n in nums_set:
            if n-1 not in nums_set:
                count = 0
                while (n+count) in nums_set:
                    count +=1
                    longest = max(count, longest)
                    
        return longest
            