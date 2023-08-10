'''
Foi requisitado que você desenvolva um programa para registrar este levantamento. O programa deverá
receber um número indeterminado de entradas, cada uma contendo: um número de identificação do mouse
o tipo de defeito:
necessita da esfera;
necessita de limpeza; a.necessita troca do cabo ou conector; a.quebrado ou inutilizado Uma identificação
igual a zero encerra o programa. Ao final o programa deverá emitir o seguinte relatório:
Quantidade de mouses: 100
Situação Quantidade Percentual
1- necessita da esfera 
2- necessita de limpeza
3- necessita troca do cabo ou conector 
4- quebrado ou inutilizado 
'''

opt = ['Necessita da esfera','Necessita de limpeza','Troca do cabo ou conector','Quebrado ou inutilizado']
problem = []
tot = 0

while True:
    ni = int(input('Número de identificação [0 p/ parar]: '))
    if ni == 0:
        break
    else:
        print('[1] Necessita da esfera;\n'
              '[2] Necessita de limpeza;\n'
              '[3] Necessita troca do cabo ou conector;\n'
              '[4] Quebrado ou inutilizado.')
        defeito = int(input('Qual o tipo de defeito? '))
        if defeito < 1 or defeito > 4:
            print('\033[1;31mERRO! Digite um valor válido\033[m')
        else:
            problem.append(defeito)
            tot += 1
    print('—'*30)
print()
print(f'Quantidade de mouses: {tot}')
print('\033[1;35m—\033[m'*58)
print(f'\033[1;35m{"SITUAÇÃO":<10}{"QUANTIDADE":>30}{"PERCENTUAL":>17}\033[m')
print('\033[1;35m—\033[m'*58)

for c in range(4):
    print(f'{c+1}. {opt[c]:<25}{problem.count(c+1):>8}{problem.count(c+1) / tot * 100:>18.1f}%')
print('\033[1;35m—\033[m'*58)  
