def isPalindrome(str):
    cleaned = ""
    cleaned = "".join(filter(lambda s: s.isalpha() or s.isnumeric(),str)).lower()
    return cleaned == cleaned[::-1]

print(isPalindrome("0P"))