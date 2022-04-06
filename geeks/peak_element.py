def peakElement(arr, n):
        id = 0    
        for i in range(0,n-1):
            if arr[i] < arr[i+1]:
                    id = i+1
        return id

print(peakElement([15], 1))