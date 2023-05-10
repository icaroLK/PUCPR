#Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida




meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def extenso(list):
    dia = list[0]
    mes = list[1]
    ano = list[2]
    mes = meses[int(list[1])-1]
    return f'{dia} de {mes} de {ano}' 
    

resp = input('Insira uma data: ').strip().replace('/', ' ').split()
print(extenso(resp))