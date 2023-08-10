tf = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
tv = [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 00]
def hour(hora,mnts):
    if hora > 12:
        hora = tf[tv.index(hora)]
        return f'São {hora:02d}:{mnts:02d} P.M.'
    elif hora == 12:
        return f'São {hora:02d}:{mnts:02d} P.M.'
    else:
        if hora == 00:
            hora = 12
        return f'São {hora:02d}:{mnts:02d} A.M.'

while True:
    hora = int(input('Digite a hora: '))
    mnts = int(input('Agora, os minutos: '))
    print(hour(hora,mnts))
    ans = str(input('Deseja continuar? ')).strip().upper()[0]
    if ans in 'N':
        break