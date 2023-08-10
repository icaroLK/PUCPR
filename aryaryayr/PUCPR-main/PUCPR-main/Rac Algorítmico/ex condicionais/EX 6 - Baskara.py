# cabeçalho
print('—'*40)
print(f'{"Calculadora de Báskara":^40}')
print('—'*40)
# coletando informações
print('Digite os valores da equação; ')
a = int(input('a (multiplica x²)= '))
b = int(input('b (multiplica x)= '))
c = int(input('c (não multiplica)= '))
# calculando
b2 = b**2
ac = 4*a*c
delta = b2 - ac
print('~'*40)
print('Para calcular a equação através de báskara, devemos primeiramente calcular o delta:')
print('delta = b² - 4ac')
# mostrando resultados
if delta >= 0:
    print(f'{b2} - (4.{a}.{c})')
    print(f'O delta é igual a {delta:.2f}')
    b3 = b * -1
    x1 = -b3 + delta**0.5
    x2 = -b3 - delta**0.5
    print('Depois, podemos calcular o "X": ')
    print('x = -b +- √delta / 2a')
    print(f'x = -{b} +- √{delta} / {2*a}')
    print(f'\033[1;35mx = {x1 / 2*a}\033[m')
    print('ou')
    print(f'\033[1;36mx = {x2 / 2*a}\033[m')
else:
    print(f'{b2} - (4.{a}.{c})')
    print(f'O delta é igual a \033[1;31m{delta:.2f}\033[m')
    print('Como o delta é negativo, não existe solução para a equação')