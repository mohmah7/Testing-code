def fac(n):
    if n == 0:
        return 1
    else:
        print (fac(n-1) * n)
        return (fac(n-1) * n)
