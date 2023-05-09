from random import randint

print('_' * 40)
print('\033[97m{:^40}\033[m'.format('CRAPS'))
print('⁻' * 40)


def jogada():
    return randint(2, 12)

rod = 1
while True:
    print(f'\n{rod}° rodada')
    dado = jogada()
    print('* Você lança os dados e tira o número: \033[34m{}\033[m *'.format(dado))

    if rod == 1:
        if dado == 7 or dado == 11:
            print('Parabéns!!!\nVocê é um \033[32mnatural\033[m e ganhou')
            break
        elif dado == 2 or dado == 3 or dado == 12:
            print('\033[31mCRAPS\033[m\nVocê Perdeu')
            break
        else:
            ponto = dado
            print(f'Seu ponto é \033[36m{ponto}\033[m, tente alcançá-lo novamente!')
    if rod != 1:
        if dado == 7:
            print('\033[31mPERDEU\033[m (tirou um 7 antes de pegar o ponto novamente)')
            break
        elif dado == ponto:
            print('\033[32mGANHOU!\033[m\nVocê alcançou seus pontos')
            break
    
    
    



    rod += 1