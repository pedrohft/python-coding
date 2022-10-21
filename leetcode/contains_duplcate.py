def containsDuplicate(a):
    d = {}

    for i in a:
        d[i] = 1+d.get(i, 0)
        # print(d.get(i, 0))

        if d.get(i, 0) >1: return True 

    # for v in d.values():
    #     if v > 1: return True
    
    return False


print(containsDuplicate([1,2,3]))