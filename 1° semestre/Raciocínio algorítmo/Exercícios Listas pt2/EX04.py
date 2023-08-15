

r = input('Insira uma frase: ').strip().title()

cu = r.lower().replace(' ', '').replace('a', '').replace(
    'e', '').replace('i', '').replace('o', '').replace('u', '')

print('A frase "{}" tem {} consoantes'.format(r, len(cu)))
