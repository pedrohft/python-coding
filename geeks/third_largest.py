class Solution:
    def thirdLargest(self,a, n):
        new_a = sorted(a)
        if len(a) < 3:
            return -1

        return new_a[-3]