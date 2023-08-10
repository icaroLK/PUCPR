def conversao(val, conv, dest, un1, un2):
    val * dest / conv
    return f'Conversão: {val:.2f} {un1} = {val * dest / conv:.2f} {un2}'
    

ano_luz = {
 "pc": 0.31,
 "al": 1,
 "ae": 63241.09,
 "ml": 525960.23,
 "sl": 31557609.92
}
unidades = ["Parsec (pc)", "Ano-Luz (al)", "Unidade Astronômica (ae)", "Minuto-Luz (ml)", "Segundo-Luz (sl)"]
count = 0

print('—'*50)
print(f'{"TABELA DE CONVERSÃO":^50}')
print('—'*50)
for unidade, valor in ano_luz.items():
    print(f'[{count+1}] {unidades[count]:<25}  ->   {valor}')
    count += 1
print('—'*50)

val = float(input('Valor a ser convertido: '))
un1 = str(input('Converter de: ')).lower()
un2 = str(input('Converter para: ')).lower()
conv = ano_luz.get(un1)
dest = ano_luz.get(un2)

print(conversao(val, conv, dest, un1, un2))