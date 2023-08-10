def valor(n):
    if n > 0:
        return 'P'
    elif n == 0:
        return 'neutro'
    else:
        return 'N'
    
n = int(input('Digite um valor: '))
print(valor(n))