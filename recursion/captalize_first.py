def capitalizeFirst(arr):
    i = [''.join(arr[0]).capitalize()]

    if len(arr) == 1:
        return [''.join(arr[0]).capitalize()]
    
    return i+capitalizeFirst(arr[1:len(arr)])


print(capitalizeFirst(['pedro','laysa','orlando']))

#Other way to resolve this question
# def capitalizeFirst(arr):
#     result = []
#     if len(arr) == 0:
#         return result
#     result.append(arr[0][0].upper() + arr[0][1:])
#     return result + capitalizeFirst(arr[1:]) 