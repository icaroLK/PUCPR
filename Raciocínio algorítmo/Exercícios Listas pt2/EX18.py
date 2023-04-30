pont = []

teste = [0] * 23  # lista com cada um dos votos nos respectivos espaços

while True:
    camisa = input('Camisa do jogador [1-23] e [0 para encerrar]: ').strip()
    if camisa == '0':
        break
    if camisa.isnumeric():
        camisa = int(camisa)
        if camisa > 23 or camisa < 1:
            print('\n\033[31mERRO\033[m\nInsira um número válido')
        else:

            pont.append(camisa)
    else:
        print('\n\033[31mERRO\033[m\nInsira um número')


print('\nRESULTADO')
print(f'Houve {len(pont)} votos')

cu = list(set(pont))
# print(pont)
cu.sort()

melhorjog = 0
melhorvot = 0

print('_'*36)
print('{:<13}{:>5}{:>18}'.format('Jogador', 'Votos', 'Porcentagem'))
for c in range(23):
    qtd = pont.count(c+1)
    teste[c] = qtd

    if qtd > melhorvot:
        melhorvot = qtd
        melhorjog = c+1

# print(teste)


melhorporc = 0
for c in cu:

    perc = float('{:.1f}'.format(teste[c-1]/len(pont)*100))

    if perc > melhorporc:
        melhorporc = perc

    print('{:<13}{:>5}{:>17}%'.format(c, teste[c-1], perc))
print('⁻'*36)


bct = teste[(teste.index(max(teste))+1)]/len(pont)*100

try:
    print('O melhor jogador foi o número {}, com {} votos, correspondendo a {}% do total de votos'.format(melhorjog, melhorvot, melhorporc))

except ValueError:
    print('Houve empate entre os melhores jogadores. O campeão será verificado na próxima votação')


