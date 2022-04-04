def getMinMax( a, n):
    
    minimum = a[0]
    maximum = a[0]
    arr = []
    for i in range(0,n):
        # maximum = a[i]
        # minimum = a[i]
        if maximum < a[i]:
            maximum = a[i]
        elif minimum > a[i]:
            minimum = a[i]
    arr.append(minimum)
    arr.append(maximum)
    return arr

print(getMinMax([3 ,2 ,1 ,56 ,1000 ,167],6))