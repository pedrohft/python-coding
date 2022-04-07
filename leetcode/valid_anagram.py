class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s) == sorted(t)
        dictS, dictT = {},{}
        
        if len(s) != len(t): return False
        
        for i in range(len(s)):
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
            dictT[t[i]] = 1 + dictT.get(t[i], 0)

        for i in s:
            if dictS[i] != dictT.get(i, 0):
                return False
        return True
            