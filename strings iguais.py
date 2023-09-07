print("DIFERENÇA ENTRE 2 STRINGS")

text1 = input("Insira o texto 1: ").strip().lower().replace(' ', '')


text2 = input("Insira o texto 2: ").strip().lower().replace(' ', '')

print(f'Texto 1: {len(text1)} caracteres\nTexto 2: {len(text2)} caracteres')


if text1 == text2:
    print('As strings são iguais')