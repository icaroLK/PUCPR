#Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida

numeros = ['Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte', 'Vinte e um', 'Vinte e dois', 'Vinte e três', 'Vinte e quatro', 'Vinte e cinco', 'Vinte e seis', 'Vinte e sete', 'Vinte e oito', 'Vinte e nove', 'Trinta', 'Trinta e um']

meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def extenso(list):
    dia = list[0]
    mes = list[1]
    ano = list[2]
    dia = numeros[int(list[0])-1]
    mes = meses[int(list[1])-1]
    return f'{dia} de {mes} de {ano}' 
    

resp = input('Insira uma data: ').strip().replace('/', ' ').split()
print(extenso(resp))

