def reverse(s):
    if not s or len(s) <= 2 or type(s) != str:
        return "not a string"
    
    backwards = []
    for i in range(len(s)-1, -1, -1):
        backwards.append(s[i])

    return ''.join(backwards)

print(reverse("Hellow my name is Pedro"))


s = "reverse"

print(s[::-1])