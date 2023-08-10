l = []
par = []
impar = []

for c in range(20):
    n = int(input('Digite um número inteiro: '))
    l.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
print(f'Números digitados: {l}')
print(f'PARES: {par}')
print(f'IMPARES: {impar}')