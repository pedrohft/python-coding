from collections import Counter

class Solution:
    def majorityElement(self, A, N):
        d = Counter(A)
    
        for k,v in d.items():
            if v > (N//2):
                return k
        return -1