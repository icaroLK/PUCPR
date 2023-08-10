A = []
for c in range(10):
    n = int(input('Digite um número: '))
    A.append(n)
sqr = []
for c in range(len(A)):
    sqr.append(A[c]**2)
for c in range(len(A)):
    if c < len(A)-1:
        print(f'{A[c]**2} +', end=' ')
    else:
        print(f'{A[c]**2} = ', end=' ')
print(sum(sqr))
