# cabeçalho
print('—'*40)
print(F'{"DIFERENÇA ENTRE DATAS":^40}')
print('—'*40)
# coletando info
l = []
dif = []
d = {}
for c in range(0, 2):
    date = input(f'Digite a {c+1}º data [dd/mm/aaaa]: ').strip().replace('/', '')
    d['Dia'] = int(date[:2])
    d['Mês'] = int(date[2:4])
    d['Ano'] = int(date[4:])
    l.append(d.copy())
# calculando
for c in range(0, 2):
    dias = 365 * l[c]['Ano'] + l[c]['Ano'] // 4 - l[c]['Ano'] // 100 \
           + l[c]['Ano'] // 400 + (l[c]['Mês'] * 306 - 91) // 10 + l[c]['Dia'] - 1
    dif.append(dias)
# resultados
print(f'A diferença entre as datas é de {abs(dif[0] - dif[1])} dias')