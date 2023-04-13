print('\033[1m{}'.format('—')*40)
print('\033[1m{:^40}\033[m'.format("VALIDAÇÃO DE CPF"))
print('\033[1m{}\033[m'.format('—')*40)

cpf = ' '
while True:
    cpf = input('Insira um CPF: ').strip().replace(' ', '').replace('-', '').replace('.', '')
    if len(cpf) == 11:
        break
    print('\nDados inválidos. Tente novamente')

CPF = []

for c in range(0,11):           #   coloca todos o cpf inteiro separado em dígitos,
    CPF.append(int(cpf[c]))    #   em forma de números inteiros, dentro de uma lista

#print(CPF)

while True:
    vez = 10
    verif1 = verif2 = soma = soma2 = 0

                                                   #soma dos digitos vezes descrescente de 10 a 2
    for c in range(0, 9):
        soma += CPF[c] * vez
        vez -= 1

    verif1 = soma * 10 % 11       #observação do PDF
    if verif1 == 10:
        verif1 = 0

    if verif1 == int(cpf[9]):
        pass
    else:
        print('O CPF digitado é \033[31mINVÁLIDO\033[m')
        break

    vez = 11
    for c in range(0, 10):
        soma2 += CPF[c] * vez
        vez -= 1


    verif2 = soma2 * 10 % 11

    if verif2 == int(cpf[10]):
        pass
    else:
        print('O CPF digitado é \033[31mINVÁLIDO\033[m')
        break
    print('CPF \033[32mVÁLIDO\033[m')
    break
