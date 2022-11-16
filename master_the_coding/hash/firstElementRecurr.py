def firstRecurr(a):
    h = {}
    for i in a:
        h[i]= 1 + h.get(i, 0)
    
        if h.get(i, 0) > 1:
            return i
    
    return "No recurring numbers"


print(firstRecurr([2,5,5,2]))