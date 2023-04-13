dec = input('Insira um número em decimal: ')
print('\n\033[1;97mDECIMAL = {}\033[m'.format(dec))
cu = int(dec)
hexa = []
while True:
    hexa.append(cu % 16)
    if cu // 16 == 0 and cu % 16 == 0 and cu == 0:
        break
    cu //= 16
hex = (((hexa[::-1])[1:]))
list = str(hex).replace('10', 'A').replace('11', 'B').replace('12', 'C').replace('13', 'D').replace('14', 'E').replace('15', 'F')
buceta = list.replace(', ', '').replace('[', '').replace(']', '')
print("\033[1;34mHexadecimal = ", buceta)
