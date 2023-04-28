atleta = []
saltos = []

while True:
    nm = input('\nNome do atleta: ').strip().title()
    if nm == '':
        break
    saltos = []
    saltos.append(nm)
    for c in range(1, 4+1):
        slt = float(input(f'{c}° salto: '))
        saltos.append(slt)

    m = sum(saltos[1:])/len(saltos[1:])

    saltos.append(m)
    atleta.append(saltos)

print('\n\nRESULTADOS')

for c in atleta:
    print('='*29)
    print(f'Atleta: {c[0]}')
    print('Saltos: ',end='')
    for oi in range(1, 4+1):
        print(c[oi], end='')
        if oi < 5-1: 
            print(' / ', end='')
    print(f'\nMédia dos saltos: {m:.2f}')