#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        a = sorted(A)
        b = sorted(B)
        flag = 1
        for i,j in zip(a,b):
                if i!=j:
                    flag = 0
                    break
                    
        
        return flag
        #return: True 