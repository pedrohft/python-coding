def reverse(strng):
    # print(strng)
    if len(strng) == 1:
        return strng[0]
        
    return strng[len(strng)-1]+reverse(strng[:-1])


print(reverse('reverse'))