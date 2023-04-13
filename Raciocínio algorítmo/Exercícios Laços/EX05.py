print("Tempo que o país 'A' com 5000000 de habitantes ultrapassará o país 'B' com 7000000 habitantes")
A = 5000000
B = 7000000
ano = 0
while A < B:
    A += (A * 3 / 100)
    B += (B * 2 / 100)
    ano += 1
print('Foram necessários {} anos'.format(ano))
