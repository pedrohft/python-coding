def isOdd(num):
    if num%2==0:
        return False
    else:
        return True
        
def someRecursive(arr, cb):
    if len(arr) > 1:
        if cb(arr[-1]):
            return True

        return someRecursive(arr[:-1],cb)
    else:
        return cb(arr[0])



print(someRecursive([0,1,2,3,4,5],isOdd))