def MissingNumber(array,n):

        for i,j in enumerate(sorted(array)):
            if (i+1) != j:
                return i+1
                
        if len(array) <= 1:
            return n
        if n not in array:
            return n
print(MissingNumber([1,2,3,4], 5))