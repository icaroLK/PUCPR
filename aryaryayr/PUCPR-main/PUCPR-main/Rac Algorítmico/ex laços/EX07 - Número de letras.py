# cabeçalho
print('—'*40)
print(F'{"NÚMERO DE LETRAS A":^40}')
print('—'*40)
# coletando info
cont = 0
l = []
while True:
    ans = str(input(f'Digite a {cont + 1}º palavra [VAZIO PARA PARAR]: ')).upper()
    a = ans.count('A')
    if a > 0:
        l.append(a)
    cont += 1
    if ans in '':
        break
# resultado
print('~' * 40)
print(f"A letra 'A' aparece \033[1;34m{sum(l)}\033[m vezes")