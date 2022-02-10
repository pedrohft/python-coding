def isPalindrome(strng):
    print(strng)
    if len(strng) == 1:
        return True
    if strng[0] != strng[-1]:
        return False
    return isPalindrome(strng[1:len(strng)-1])



print(isPalindrome('madam'))
