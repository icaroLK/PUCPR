print('\033[1;35m—\033[m'*30)
print(f'\033[1;35m{"GASTOS COM ABONO":^30}\033[m')
print('\033[1;35m—\033[m'*30)

salario = []
abono = []
minimo = []
cont = 1

while True:
    bruto = float(input(f'{cont}º salário [0 p/ parar]: R$'))
    if bruto < 0:
        print('ERRO! Digite um salário válido.')
    elif bruto == 0:
        break
    else:
        salario.append(bruto)
        cont += 1

for c in range(len(salario)):
    if salario[c] <= 500:
        abono.append(100)
        minimo.append(1)
    else:
        porc = salario[c] * 0.2
        abono.append(porc)

print('\033[1;35m—\033[m'*30)
print(f'\033[1;35m{"SALÁRIOS":<12} - {"ABONOS":>12}')
print('\033[1;35m—\033[m'*30)
for c in range(len(salario)):
    print(f'R${salario[c]:<10.2f} - \t    R${abono[c]:.2f}')
print('\033[1;35m—\033[m'*30)
print(f'Foram processados {cont-1} trabalhadores.')
print(f'Total gasto com abonos: {sum(abono)}')
print(f'Valor mínimo pago à {len(minimo)} colaboradores')
print(f'Maior valor gasto com abono: R${max(abono)}')
print('\033[1;35m—\033[m'*30)