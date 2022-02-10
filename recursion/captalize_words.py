def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    s = arr[0]
    result.append(s.upper())
    return result + capitalizeWords(arr[1:len(arr)])

print(capitalizeWords(['pedro','laysa']))
