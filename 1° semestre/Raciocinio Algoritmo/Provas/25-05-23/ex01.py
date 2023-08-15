dic = {}

while True:
    liq = input('Qual líquido? (sair para sair)')
    if liq == 'sair':
        break
    qtd = float(input('Quantidade em litros: '))
    if liq in dic:
        dic[liq] += qtd
    else:
        dic[liq] = qtd


print(dic)