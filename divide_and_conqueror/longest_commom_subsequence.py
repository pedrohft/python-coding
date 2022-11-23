def find_lcs(s1,s2,index1,index2):
    if len(s1) == index1 or len(s2) == index2:
        return 0
    if s1[index1] == s2[index2]:
        return 1 + find_lcs(s1,s2,index1+1, index2+1)
    else:
        op1 = find_lcs(s1,s2,index1, index2+1)
        op2 = find_lcs(s1,s2, index1+1, index2)
        return max(op1,op2)

print(find_lcs("elephant", "eretpat", 0, 0))