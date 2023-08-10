# cabeçalho
print('—'*40)
print(F'{"NOME E SOBRENOME":^40}')
print('—'*40)
# coletando info
while True:
    name = str(input('Digite seu nome completo: ')).strip().split()
# resultados
    print(f'Seu \033[1;34mprimeiro\033[m nome é : {name[0].capitalize()}')
    print(f'Seu \033[1;36múltimo\033[m nome é: {name[len(name)-1].capitalize()}')
    ans = str(input('Deseja continuar? [S/N] ')).upper()
    if ans in 'N':
        break