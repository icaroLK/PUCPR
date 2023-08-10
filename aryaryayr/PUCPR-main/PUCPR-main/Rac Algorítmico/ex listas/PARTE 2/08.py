i = []
h = []

for c in range(5):
    idade =int(input('Digite sua idade: '))
    i.append(idade)
    altura0 = input('Digite sua altura (m): ').replace(',', '.')
    altura = float(altura0)
    h.append(altura)
for c in range(5):
    print(f'{c+1}ª pessoa: {h[c]:.2f} centímetros, {i[c]} anos')