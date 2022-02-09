def power(x,y):
    assert y>=0 and int(y) == y , 'The number has to be a positive integer only!'
    if y == 0:
        return 1
    return x*power(x,y-1)

print(power(2,4))