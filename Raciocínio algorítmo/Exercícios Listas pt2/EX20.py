salarios = []
abonos = []
qtd_colabora = 0 #quantidade de salários colocados / qtd de colaboradores
qtd_abono_min = 0 #quantidade de abonos mínimos dados
tot_abonos = 0 #soma de todos os abonos
maior_abono = 0


while True:
    resp = input('Salário: R$').strip()
    if resp == '0':
        break
    try:
        salario = float(resp)
        salarios.append(salario)
        qtd_colabora += 1
    except ValueError:
        print('Insira um valor válido!')



for c in salarios:
    valor_abono = c/100*20
    if valor_abono <= 100:
        valor_abono = 100
        qtd_abono_min += 1
    if valor_abono > maior_abono:
        maior_abono = valor_abono
    tot_abonos += valor_abono
    abonos.append(valor_abono)



print('_'*42)
print('      {:<13}{:>10}'.format('Salário', 'Abono'))
print('⁻'*42)


for c in range(len(salarios)):
    print('   R$ {:<15.2f}R${:>10.2f}'.format(salarios[c], abonos[c]))
print('_'*42)
print('\nForam processados {} colaboradores'.format(qtd_colabora))
print('Total gasto com abonos: R$ {:.2f}'.format(tot_abonos))
print('Valor mínimo pago a {} colaboradores'.format(qtd_abono_min))
print('Maior valor de abono pago: R$ {:.2f}\n\n'.format(maior_abono))
