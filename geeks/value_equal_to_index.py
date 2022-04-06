#User function Template for python3
class Solution:

	def valueEqualToIndex(self,arr, n):
			# code here
			a = []
			for i in range(0, n):
				if arr[i] == (i+1):
					a.append(arr[i])
			
			return a