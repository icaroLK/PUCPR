def potencia(num, n):
    return num**n

def pot_recursiva(num, n):
    if n == 0:
        return 1
    return num * pot_recursiva(num, n-1)


num = int(input('Digite um número inteiro: '))
n = int(input('Digite uma potência inteira: '))

print(f'Função normal: {potencia(num, n)}')
print(f'Função recursiva: {pot_recursiva(num, n)}')