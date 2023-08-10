#cabeçalho
print('—'*40)
print(f'{"Peso Ideal":^40}')
print('—'*40)

#coletando informações
sex = str(input('Digite seu sexo [M/F]: ')).upper()
altura = float(input('Digite sua altura (cm): '))
pIdeal = 0

#calculando e mostrando resultados
if sex in 'M':
    pIdeal = (72.7 * altura / 100) - 58
    print(f'O seu peso ideal é {pIdeal:.1f} kg')
elif sex in 'F':
    pIdeal = (62.1 * altura / 100) - 44.7
    print(f'O seu peso ideal é {pIdeal:.1f} kg')