# cabeçalho
print('—'*40)
print(f"{'VALIDANDO CPFs':^40}")
print('—'*40)
l = []
val = n = val2 = n2 = 0
# coletando info
while True:
    cpf = input('Digite seu CPF: ').strip().replace('.','').replace('-','')
    if len(cpf) != 11:
        print('ERRO! Digite um CPF legível.')
    if len(cpf) == 11:
        for c in range(0, 11):
            l.append(int(cpf[c]))
        break
# calculando e mostrando resultados
while True:
    cont = 10
    for c in range(0, 9):
        n += int(l[c]) * cont
        cont -= 1
    val = n * 10 % 11
    if val == 10:
        val = 0
    if val == l[9]:
        pass
    elif val != l[9]:
        print('CPF \033[1;31mINVÁLIDO\033[m')
        break

    cont2 = 11
    for i in range(0,10):
        n2 += int(l[i]) * cont2
        cont2 -= 1
    val2 = n2 * 10 % 11
    if val2 == 10:
        val2 = 0
    if val2 == l[10]:
        print('CPF \033[1;32mVÁLIDO\033[m')
        break
    elif val2 != l[10]:
        print('CPF \033[1;31mINVÁLIDO\033[m')
        break