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
print(f'A diferença de dias é de {oi}')
