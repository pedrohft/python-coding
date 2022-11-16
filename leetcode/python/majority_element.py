def majority(nums):
    h = {}

    for i in nums:
        h[i] = 1+h.get(i, 0)
    
    for k,v in h.items():
        if v > len(nums)//2:
            return k
    return -1

print(majority([2,2,2,1,4,5,6,2,2]))