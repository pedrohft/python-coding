def minAnd2ndMin( a, n):
    #code here
    new = sorted(list(set(a)))
    if len(new) <= 1: return [-1]
    return new[0:2]


print(minAnd2ndMin([1,1,1,1,1],5))