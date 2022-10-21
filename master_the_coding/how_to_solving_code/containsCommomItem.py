from array import array


def constainsCommonItems(array1, array2):
    d = dict()
    
    #   for i in range(len(array1)):
    #     d[array1[i]] = True

    d = {array1[i]: True for i in range(0, len(array1))}
    for x in array2:
        if x  in d:
            return True
    return False


print(constainsCommonItems(["a","b",1], ["a",1,"e"]))
#FROM O(N^2) to O(n)