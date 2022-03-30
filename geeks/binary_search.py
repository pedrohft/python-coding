class Solution:	
	def binarysearch(self, arr, n, k):
		# code here
            l = 0
            h = n-1

            while l <= h:
                m = l + (h-l)//2
                
                x = arr[m]

                if x == k:
                    return m
                
                elif x < k:
                    l = m + 1 
                
                elif x > k:
                    h = m - 1 
                    
            return -1