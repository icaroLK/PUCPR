d = {}

while True:
    bebida = str(input('Digite o nome da bebida (0 p/ parar): '))
    if bebida in '0':
        break
    quant = int(input('Digite a quantidade (ml): '))
    if bebida in d:
        d[bebida] += quant
    else:
        d[bebida] = quant

for k, v in d.items():
    print(f'{k} -> {v}')