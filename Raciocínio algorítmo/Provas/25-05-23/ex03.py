def elev(num, n):
    if n < 0:
        return "O expoente deve ser maior ou igual a zero"
    elif n == 0:
        return 1
    else:
        result = num ** n
        return result

print(elev(5,3))