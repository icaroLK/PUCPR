cars = []
consumo = []
L = []

for c in range(5):
    print(f'Veículo {c+1}')
    car = str(input('Modelo: ')).title()
    km = float(input('Consumo: '))
    cars.append(car)
    consumo.append(km)
    print()
for c in range(5):
    litros = 1000 / consumo[c]
    L.append(litros)
print('\033[1;35mRELATÓRIO FINAL\033[m')
for c in range(5):
    print(f'{c+1}. {cars[c]:<10} - {consumo[c]:>8}  -  {L[c]:>8.1f} litros - R${L[c]*2.25:>8.2f}')

menor = consumo.index(max(consumo))
print(f'O de menor consumo é {cars[menor]}')