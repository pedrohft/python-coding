def valid(p1, p2):
    print(p1,p2)
    if p1 ==  "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False
    
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        if s[0] in ")}]": return False
        if len(s) <= 1: return False

        f = True

        for i in s:
            if i in ")}]" and len(stack) > 0:
                f = valid(stack.pop(), i)

                if f == False:
                    return f
                else: continue

            stack.append(i)

        if len(stack) > 0:
            return False
        return f