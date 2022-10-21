def findMissing(a, n):
    sum1 = n*(n+1)/2
    sum2 = sum(a)
    return sum1 - sum2

print(findMissing([1,2,3,5], 5))