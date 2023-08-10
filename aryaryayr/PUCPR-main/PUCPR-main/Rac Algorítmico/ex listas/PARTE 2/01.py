l = []
for c in range(5):
    n = int(input('Digite um número inteiro: '))
    l.append(n)
print(f'Você digitou os números:', end=' ')
for item in l:
    print(item, end=', ')