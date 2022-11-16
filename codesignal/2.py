def solution(arr):
    d = {}
    for s in arr:
        for i, l in enumerate(s):
            d[i] = str(d.get(i, '')) + l
    s = ""       
    for k,v in d.items():
        s = s+v
    return s

print(solution(["Daisy", 
 "Rose", 
 "Hyacinth", 
 "Poppy"]))

#  DRHPaoyoisapsecpyiynth