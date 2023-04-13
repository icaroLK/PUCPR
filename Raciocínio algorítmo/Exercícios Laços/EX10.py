list = []
dic = {}
dif = []
for c in range(2):
    data = input('Insira uma data (no formato dd/mm/aaaa): ').strip().replace('/','')
    dic['Dia'] = int(data[:2])
    dic['Mes'] = int(data[2:4])
    dic['Ano'] = int(data[4:])
    list.append(dic.copy())

for c in range(2):
    dias = 365 * list[c]['Ano'] + list[c]['Ano'] // 4 - list[c]['Ano'] // 100 + list[c]['Ano'] // 400 + (list[c]['Mes'] * 306 - 91) // 10 + list[c]['Dia'] - 1
    dif.append(dias)

oi = abs(dif[0] - dif[1])
print(f"A diferença de dias entre {list[0]['Dia']:02d}/{list[0]['Mes']:02d}/{list[0]['Ano']} "
      f"e {list[1]['Dia']:02d}/{list[1]['Mes']:02d}/{list[1]['Ano']} é de {oi} dias")








#comecei a tentar aqui ai fiz do jeito que ta em cima
'''list = []
dic = {}

for c in range(2):
    data = input('Insira uma data (no formato dd/mm/aaaa): ').strip().replace('/','')
    dic['Dia'] = int(data[:2])
    dic['Mes'] = int(data[2:4])
    dic['Ano'] = int(data[4:])
    list.append(dic.copy())


difano = abs(list[0]['Ano'] - list[1]['Ano'])
#ja tenho info da diferença de anos, so no final multiplicar por 365/366 e somar com a diferença de dias


difmes = abs(list[0]['Mes'] - list[1]['Mes'])


difdia = abs(list[0]['Dia'] - list[1]['Dia'])

print(difano)
print()
print(difmes)
print()
print(difdia)'''