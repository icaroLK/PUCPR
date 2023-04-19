#  A senha deve ter mínimo 8 e máximo 15 caracteres.
#  A senha deve ter pelo menos uma letra maiúscula.
#  A senha deve ter pelo menos uma letra minúscula.
#  A senha deve ter pelo menos um símbolo. Ex: * ! # $ % & + - / : ; = ? @ \ |
#  A senha deve ter pelo menos um número.


from random import randint, choice

num = [0,1,2,3,4,5,6,7,8,9]
alphaP = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphaG = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T', 'U','V','W','X','Y','Z']
eps = ['*', '!', '#', '$', '%', '&', '+', '-', '/', ':', ';', '=', '?', '@','|']
paw = [ ]
n = 0
ap = 0
ag = 0
e = 0


while True:
    paw.append(str(input('Digite sua senha, ela deve conter:\nDe 8 a 15 caraceres\nPelo menos uma letra maiuscula e maiusvcula\nUma caractere especial\nSenha: ')))
    if len(paw) >= 8 and len(paw) <= 15:   
        for c in paw:
            if c in num:
                n+=1
            if c in alphaP:
                ap+=1 
            if c in alphaG:
                ag+=1
            if c in esp:
                e+=1 
        if n >= 1 and c >= 1 and ag >= 1 and ap >= 1:
            print('Sua senha é valida')
            print(f'Sua senha é: {paw}')
            print(f'Sua senha contem {len(paw)} sendo {ap} letras minusculas, {ag} letras maiusculas, {num} números e {e} caracteres especiais')
            break 
    else: 
        print('Esta faltando algum requisito...')
