##This solution get time limit exceeds
def duplicates(arr, n):
    d = {}
    aux = []
    for i in arr:
        d[i] = arr.count(i)

    for k,v in d.items():
        if v > 1:
            aux.append(k)
    if not aux:
        return [-1]
    
    return sorted(aux)



print(duplicates([10, 10 ,7 ,7 ,7 ,4 ,0 ,5 ,10 ,5 ,10],11))

##Final solution
from collections import Counter

class Solution:
    def duplicates(self, arr, n):
        d = {}
        aux = []
        d = Counter(arr)
    
        for k,v in d.items():
            if v > 1:
                aux.append(k)
        if not aux:
            return [-1]
        
        return sorted(aux)
    	# code here