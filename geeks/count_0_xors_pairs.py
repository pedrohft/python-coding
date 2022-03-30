from collections import Counter


def calculate (arr, n) : 
    #Complete the function
    xor = 0
    
    for i in range(0, n):
        for j in range(i,n):
            if((arr[i] != arr[j]) == 0 and i!=j):
                xor+=1
            print(i,j)

    return xor


print(calculate([16, 19 ,12 ,2 ,9 ,11 ,14 ,5 ,13 ,7 ,3 ,18 ,14 ,2 ,2 ,8], 16))