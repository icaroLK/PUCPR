escolhas = []

print('''
1 - Necessita de esfera
2 - Necessita de limpeza
3 - Necessita troca do cabo ou conector
4 - Quebrado ou inutilizado
0 - Sair''')

while True:
    resp = input('R: ').strip()
    if resp == '0':
        break
    try:
        esc = int(resp)
        if esc > 4 or esc < 1:
            print('Insira um valor válido')
        else:
            escolhas.append(esc)
    except ValueError:
        print('Insira um número')




print(f'{escolhas.count(1)} mouses precisam de esfera ({escolhas.count(1)/len(escolhas)*100:.1f}%)')
print(f'{escolhas.count(2)} mouses precisam de limpeza ({escolhas.count(2)/len(escolhas)*100:.1f}%)')
print(f'{escolhas.count(3)} mouses precisam de troca do cabo ou conector ({escolhas.count(3)/len(escolhas)*100:.1f}%)')
print(f'{escolhas.count(4)} mouses estão quebrados ou inutilizados ({escolhas.count(4)/len(escolhas)*100:.1f}%)')