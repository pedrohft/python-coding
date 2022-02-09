def gcp(a,b):
    assert int(a) == a and int(b) == b, "Only integer numbers"

    if a < 0 or b < 0:
        a = -1 * a
        b = -1 * b

    if b==0:
        return a
    return gcp(b,a%b)


print(gcp(48,18))