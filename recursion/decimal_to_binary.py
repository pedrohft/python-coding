def decimal_to_binary(n):
    assert n>=0 and int(n) == n , 'The number has to be a positive integer only!'
    if n == 0:
        return 0
    return n%2 + 10 * decimal_to_binary(int(n/2))

print(decimal_to_binary(13))