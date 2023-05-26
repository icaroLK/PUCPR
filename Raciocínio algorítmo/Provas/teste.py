def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        sequence.append(sequence[-1] + sequence[-2])
        return sequence

# Exemplo de uso
n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))
resultado = fibonacci(n)
print("Sequência de Fibonacci até o", n, "º termo:")
print(resultado)
