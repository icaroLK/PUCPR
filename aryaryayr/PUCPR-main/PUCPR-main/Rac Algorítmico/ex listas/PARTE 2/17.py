ordem = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
saltos = []
nome = str(input('Atleta: ')).title()
for c in range(5):
    salto = float(input(f'{ordem[c]} salto: '))
    saltos.append(salto)
print()
print('Resultado final: ')
print(f'Atleta: {nome}')
print(f'Saltos: ', end=' ')
for v, i in enumerate(saltos):
    if v < len(saltos)-1:
        print(i, end=' - ')
    else:
        print(i)
print(f'Média: {sum(saltos)/len(saltos)}')