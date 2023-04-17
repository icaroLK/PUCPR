pond = [ ]
dic = { }
nt = 0

print('\033[1;97m{}'.format('—')*40)
print('\033[1;97m{:^40}\033[m'.format('CALCULADORA DE MÉDIA'))
print('\033[1;97m{}\033[m'.format('—')*40)



resp = int(input('1 - Média aritmética\n2 - Média ponderada\nR: '))


if resp == 1:
    print('\033[1;97m{}'.format('—')*40)
    print('\033[1;97m{:^40}\033[m'.format('Média aritmética'))
    print('\033[1;97m{}\033[m'.format('—')*40)


    qtd = int(input('Insira a quantidade de notas: '))
    for c in range(qtd):
        nota = float(input('Insira a nota da {}° prova: '.format(c+1)))
        nt += nota
    m = nt / qtd



if resp == 2:
    print('\033[1;97m{}'.format('—')*40)
    print('\033[1;97m{:^40}\033[m'.format('Média ponderada'))
    print('\033[1;97m{}\033[m'.format('—')*40)


    qtd = int(input('Insira a quantidade de notas: '))
    for c in range(qtd):
        print('—'*8)
        peso = float(input('PROVA {}\nPeso: '.format(c+1)))
        nota = float(input('Nota: '))
        dic[peso] = nota
        pond.append(dic)
        print(pond) #TESTE PRA VER SE TA FUNCIONADNO

    for v, i in enumerate(pond):
        print('i:', i)
        print('v:', v)
        print(i[v])
        print(i[v+1])
        print()
        print()


        

#    m = nt / qtd








print('\nA sua média foi {:.1f}'.format(m))