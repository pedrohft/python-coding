#User function Template for python3

class Solution:
    def countZeroes(self, arr, n):
        # code here
        count = 0
        a = sorted(arr)
        for i in a:
            if i <= 0:
                count+=1
            else: break
        return count