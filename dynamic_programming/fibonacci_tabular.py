def fibo(n):
    tab = [0,1]

    for i in range(2,n+1):
        tab.append(tab[i-1]+tab[i-2])
    return tab[n-1]

print(fibo(6))