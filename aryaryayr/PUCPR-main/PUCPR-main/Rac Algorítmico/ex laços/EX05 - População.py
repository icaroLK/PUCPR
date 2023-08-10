# cabeçalho
print('—'*40)
print(F'{"TAXA DE NATALIDADE":^40}')
print('—'*40)
# calculos
a = a1 = 5000000
b = b1 = 7000000
cont = 0
while True:
    a += a * 0.03
    b += b * 0.02
    cont += 1
    if a > b:
        break
# resultados
print('~' * 40)
print(f'País A = {a1} habitantes.(3% de taxa de natalidade)')
print(f'País B = {b1} habitantes. (2% de taxa de natalidade)')
print('~' * 40)
print(f'Após {cont} anos, o país A terá {a:.1f} habitantes e o país B terá {b:.1f} habitantes'
      f'\n{a - b:.1f} habitantes de diferença.')