from operator import le


def subArraySum(arr, n, s):
    current_sum = arr[0]
    left = 0
    right = 0

    while left < n and right < n:
        if current_sum == s:
            return left+1, right+1
        if current_sum < s and right < n-1:
            right+=1
            current_sum += arr[right]
        else:
            current_sum -= arr[left]
            left+=1
    return [-1]
    
print(subArraySum([1,2,3,7,5], 5,12))
