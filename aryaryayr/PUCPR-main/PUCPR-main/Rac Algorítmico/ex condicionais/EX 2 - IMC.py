from time import sleep

#cabeçalho
print('—'*40)
print(f'{"Cálculo do IMC":^40}')
print('—'*40)

#coletando informações
peso = float(input('Digite seu peso (Kg): '))
altura = float(input('Digite sua altura (cm): '))
imc = peso / (altura/100) ** 2
print('Calculando seu IMC...')
sleep(1)

#calculando e mostrando resultados
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f}')
    print('Você está \033[1;33mabaixo do peso\033[m!')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.2f}')
    print('Você está com o peso \033[1;32mnormal\033[m.')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.2f}')
    print('Você está \033[1;34macima do peso\033[m!')
else:
    print(f'Seu IMC é {imc:.2f}')
    print('Você está com \033[1;31mOBESIDADE\033[m!')