print('\033[1m{}'.format('—')*40)
print('\033[1m{:^40}\033[m'.format("CALENDARINHO :)"))
print('\033[1m{}\033[m'.format('—')*40)

dia = str(input('Insira o dia do seu aniversário: '))
mes = str(input('Insira o mês do seu aniversário (Ex: 07): '))
idade = str(input('Insira sua idade: '))

ano = 2023 - int(idade)

abrev = ['janeiro' , 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
         'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

form = input('''\nEscolha a forma de visualização da data:
[1] Data simples
[2] Data abreviada
[3] Data completa
R: ''')

if form in '1':
    print('\nVocê nasceu em {}/{}/{}'.format(dia, mes, ano))

if form in '2':
    print('\nVocê nasceu em {}/{}/{}'.format(dia, abrev[int(mes)-1][:3], ano))
                                                    #eu poderia ter deixado o int junto com o input e poupar
                                                    #esse trabalho aqui, mas queria testar fazer esse tipo de
                                                    #manipulaçao de texto/lista ai fiz assim

if form in '3':
    print('\nVocê nasceu em {} de {} de {}'.format(dia, abrev[int(mes)-1], ano))











#outro jeito, sem pedir aniverário

'''print('\033[1m{}'.format('—')*40)
print('\033[1m{:^40}\033[m'.format("CALENDARINHO :)"))
print('\033[1m{}\033[m'.format('—')*40)


data = str(input('Insira sua data de nascimento (Ex: 24 08 2004): '))

dia = data.split()[0]
mes = data.split()[1]
ano = data.split()[2]

abrev = ['janeiro' , 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho',
         'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

form = input('\nEscolha um formato: \n[1] Data simples. Ex: 10/05/2005 \n[2] Data abreviada. Ex: 10/ago/1994 
\n[3] Data completa Ex: 18 de junho de 1987\nR: ')

if form in '1':
    print('\nSua data de nascimento é {}/{}/{}'.format(dia, mes, ano))

if form in '2':
    print('\nSua data de nascimento é {}/{}/{}'.format(dia, abrev[int(mes)-1][:3], ano))

if form in '3':
    print('\nSua data de nascimento é {} de {} de {}'.format(dia, abrev[int(mes)-1], ano))'''
