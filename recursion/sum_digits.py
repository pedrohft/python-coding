def sum_digit(n):
    assert n>=0 and int(n) == n , 'The number has to be a positive integer only!'
    if n in [0,1]:
        return n
    return n%10 + sum_digit(n//10)

print(sum_digit(1234))