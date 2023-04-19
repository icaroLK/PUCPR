#  A senha deve ter mínimo 8 e máximo 70 caracteres.
#  A senha deve ter pelo menos uma letra maiúscula.
#  A senha deve ter pelo menos uma letra minúscula.
#  A senha deve ter pelo menos um símbolo. Ex: * ! # $ % & + - / : ; = ? @ \ |
#  A senha deve ter pelo menos um número.


from random import randint, choice

num = [0,1,2,3,4,5,6,7,8,9]
alphaP = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphaG = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T', 'U','V','W','X','Y','Z']
non = ['*', '!', '#', '$', '%', '&', '+', '-', '/', ':', ';', '=', '?', '@','|']
tud = [num, alphaP, alphaG, non]
paw = [ ]
esc = [0,1,2,3] 

qtd = int(input('Quantidade de caracteres [8-15]: '))

c = 0
while True:

    esc.append(alt)
    print(esc)
    paw.append(choice(tud[alt]))
    print(paw)
    if len(paw) == qtd:
        print('entrou')
        if 1 and 2 and 3 and 4 in esc:
            print('deu boa')
            print(paw)
            break
        else:
            paw = [ ]
    c += 1
    if c == 100:
        break

# for c in range(qtd):
#     esc.append(alt)
#     paw.append(choice(tud[alt]))
#     print(paw)
