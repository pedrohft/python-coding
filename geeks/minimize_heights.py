class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr =  sorted(arr)
        asn = arr[n-1] - arr[0]
        smallest = arr[0]+k
        largest = arr[n-1]-k
        
        for i in range(0,n-1):
            mi = min(smallest, arr[i+1]-k)
            ma = max(largest, arr[i]+k)
            asn = min(asn, ma-mi)
        return asn