# cabeçalho
print('—'*40)
print(F'{"MASSA DE UM MATERIAL":^40}')
print('—'*40)
# coletando info
mat = float(input('Digite a massa do material (g): '))
cont = 0
mat2 = mat
# calculando e mostrando resultados
while True:
    mat -= mat / 2
    cont += 50
    if mat < 0.5:
        break
print(f'Um material com {mat2} gramas demoraria'
      f' {cont} segundos para ter sua massa menor que 0.5g.')