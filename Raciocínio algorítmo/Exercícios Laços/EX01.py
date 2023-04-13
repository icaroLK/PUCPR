print('Material radioativo')
m = int(input('Insira a massa em gramas: '))
c = 0
while m >= 0.5:
    m = m / 2
    c += 1
print('A massa final é de {:.2f}g e durou {}s'.format(m, c*50))
