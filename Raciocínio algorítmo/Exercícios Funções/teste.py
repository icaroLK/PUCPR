def data(date):
    l = []
    l.append(date[:2])
    l.append(date[2:4])
    l.append(date[4:])
    mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
         'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    for c in range(len(mes)):
        if c == int(l[1]):
            return f'DATA EM EXTENSO: {l[0]} de {mes[c]} de {l[2]}'


date = input('Digite uma data [dd/mm/aaaa]: ').strip().replace('/', '')
print(data(date))