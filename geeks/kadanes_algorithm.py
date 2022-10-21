class Solution:
    # def maxSubArraySum(self,arr,N):
    #     max_so_far = -9999999
    #     max_ending_here = 0

    #     for i in range(0,N):
    #         max_ending_here += arr[i]

    #         if (max_so_far) < max_ending_here:
    #             max_so_far = max_ending_here
            
    #         if (max_ending_here < 0):
    #             return -1
    #     return max_so_far

    def maxSubArraySum(self, a, N):
        max_so_far =a[0]
        max_ending_here = a[0]

        for i in range(1, N):
            max_ending_here = max(a[i], max_ending_here + a[i])
            max_so_far = max(max_so_far, max_ending_here)

        return max_so_far

a = [-13, -3, -25, -20, -3, -16, -23, -12, -5, -22, -15, -4, -7]
print("Maximum contiguous sum is", Solution.maxSubArraySum(a,len(a)))


