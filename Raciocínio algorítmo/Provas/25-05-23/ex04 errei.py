def elev(num, n):
    if n == 0:
        return 1
    elif n < 0:
        return 1 / elev(num,-n)
    elif n % 2 == 0:
        temp = elev(num, n//2)
        return temp ** temp
    else:
        return num * elev(num, n-1)


print(elev(5,3))