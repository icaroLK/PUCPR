notas = []
cont = 1
while True:
    n = float(input(f'Digite a {cont}ª nota [-1 p/ parar]: '))
    if n != -1:
        notas.append(n)
        cont += 1
    if n == -1:
        break
print('[1] Mostre a quantidade de valores que foram lidos;\
        \n[2] Exiba todos os valores na ordem em que foram informados, um ao lado do outro;\
        \n[3] Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;\
        \n[4] Calcule e mostre a soma dos valores;\
        \n[5] Calcule e mostre a média dos valores;\
        \n[6] Calcule e mostre a quantidade de valores acima da média calculada;\
        \n[7] Calcule e mostre a quantidade de valores abaixo de sete;\
        \n[8] Encerrar o programa.')
while True:
    print('-' * 30)
    ans = int(input('O que deseja fazer? '))
    if ans == 1:
        print(f'Foram lidos {len(notas)} valores.')
    elif ans == 2:
        print(f'NOTAS: ', end=' ')
        for n in notas:
            print(n, end=' - ')
        print('FIM')
    elif ans == 3:
        notas.reverse()
        for n in notas:
            print(n)
    elif ans == 4:
        print(f'Soma dos valorws: {sum(notas):.1f}')
    elif ans == 5:
        print(f'Média dos valores: {sum(notas)/len(notas):.1f}')
    elif ans == 6:
        for n in notas:
            if n > sum(notas)/len(notas):
                print(n, end=' - ')
        print('FIM')
    elif ans == 7:
        for n in notas:
            if n < 7:
                print(n, end=' - ')
        print('FIM')
    elif ans == 8:
        break
print('Obrigado pela preferência!')
