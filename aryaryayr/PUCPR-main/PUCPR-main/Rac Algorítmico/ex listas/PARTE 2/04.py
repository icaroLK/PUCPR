l = []
for c in range(10):
    letter = str(input('Digite uma letra: ')).upper()
    if letter not in 'AEIOU':
        l.append(letter)
print(f'Foram lidas {len(l)} consoantes: ')
for cons in l:
    print(cons, end=', ')