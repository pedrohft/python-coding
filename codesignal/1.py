def solution(numbers, left, right):
    arr = [False]*len(numbers)
    
    for i in range(len(numbers)):
        
        for j in range(left, right+1):
            r = (i + 1) * j
            if (r == numbers[i]):
                arr[i] = True
        
    return arr

print(solution([1,2,3,4,5], 1, 1))