# cabeçalho
print('—'*40)
print(F'{"NÚMEROS COM RESTO 5":^40}')
print('—'*40)
# resultados
print('Os números entre 1000 e 1999 que divididos por 11 tem resto 5 sâo')
for c in range(1000, 2000):
    if c % 11 == 5:
        print(c, end=', ')
    if c == 1237 or c == 1490 or c == 1732 or c == 1996:
        print()