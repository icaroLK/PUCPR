from random import randint, choice

num = [0,1,2,3,4,5,6,7,8,9]
alphaP = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
alphaG = ['A', 'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T', 'U','V','W','X','Y','Z']
non = ['*', '!', '#', '$', '%', '&', '+', '-', '/', ':', ';', '=', '?', '@','|']
tud = [num, alphaP, alphaG, non]
paw = [ ]

qtd = int(input('Quantidade de caracteres [8-15]: '))

c = 0
while True:
    paw.append(choice(choice(tud)))
    print('oi')
    if len(paw) == qtd:
        for c in range(len(num)):
            if num[c] in paw:
                pass
            else:
                print('tem nao kkkk')
                paw = [ ]

        for c in range(len(alphaG)):
            if alphaG[c] in paw:
                pass
            else:
                paw = [ ]

        for c in range(len(alphaP)):
            if alphaP[c] in paw:
                pass
            else:
                paw = [ ]

        for c in range(len(non)):
            if non[c] in paw:
                pass
            else:
                paw = [ ]
        break

    c += 1
    if c == 100:
        break

print(paw)