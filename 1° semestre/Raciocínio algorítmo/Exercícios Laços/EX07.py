resp = ' '
list = []
c = 0
while resp != '':
    resp = input('Insira uma palavra (Deixe vazio para parar): ').lower()
    list += resp
    c += 1
print("Existem {} letras 'A' nas {} palavras digitadas".format(list.count('a'), c-1))