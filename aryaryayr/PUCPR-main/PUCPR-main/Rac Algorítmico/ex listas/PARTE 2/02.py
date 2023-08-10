l = []
for c in range(10):
    n = int(input('Digite um número: '))
    l.append(n)
l.sort(reverse=True)
print(f'Seus números em ordem inversa são: {l}')