tot = [ ]
provas = []
nt = 0
pesao = 0
cima = 0

print('\033[1;97m{}'.format('—')*40)
print('\033[1;97m{:^40}\033[m'.format('CALCULADORA DE MÉDIA'))
print('\033[1;97m{}\033[m'.format('—')*40)



resp = int(input('1 - Média aritmética\n2 - Média ponderada\n3 - Calcular quanto falta para passar\nR: '))


if resp == 1:
    print('\033[1;97m{}'.format('—')*40)
    print('\033[1;97m{:^40}\033[m'.format('Média aritmética'))
    print('\033[1;97m{}\033[m'.format('—')*40)


    qtd = int(input('Insira a quantidade de notas: '))
    for c in range(qtd):
        nota = float(input('Insira a nota da {}° prova: '.format(c+1)))
        nt += nota
    m = nt / qtd
    print('\nA sua média foi {:.1f}'.format(m))


if resp == 2:
    print('\033[1;97m{}'.format('—')*40)
    print('\033[1;97m{:^40}\033[m'.format('Média ponderada'))
    print('\033[1;97m{}\033[m'.format('—')*40)


    qtd = int(input('Insira a quantidade de notas: '))
    for c in range(qtd):
        print()
        print('—'*12)
        print('   PROVA {}'.format(c+1))
        print('—'*12)
        peso = float(input('Peso: '))
        nota = float(input('Nota: '))
        print('—'*12)
        pesao += peso
        provas.append(peso)
        provas.append(nota)
        tot.append(provas)
        provas = [ ]

    for c in range(qtd):
        cima += (tot[c][0] * tot[c][1])

    m = cima / pesao
    print('\nA sua média foi {:.1f}'.format(m))
        

if resp == 3:
    print('\033[1;97m{}'.format('—')*40)
    print('\033[1;97m{:^40}\033[m'.format('Nota faltante'))
    print('\033[1;97m{}\033[m'.format('—')*40)
    mini = float(input('Insira a média necessária para passar: '))
    qtd = int(input('Insira a quantidade de notas: '))

    for c in range(qtd-1):
        nota = float(input('Insira a nota da {}° prova: '.format(c+1)))
        nt += nota
    # n = nt / qtd
    x = (mini * qtd) - nt
    print('Você precisa tirar no mínimo {:.2f} na próxima prova para passar de ano'.format(x))


print('\nobrigado, volte sempre :)')

