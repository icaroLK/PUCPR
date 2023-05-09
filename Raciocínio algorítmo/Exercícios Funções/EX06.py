# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.





def convert(hora, minuto):
    newhora = hora - 12
    if hora <= 12:
        sun = 'A.M'
    else:
        sun = 'P.M'
    return '{:02d}:{:02d} {}'.format(newhora, minuto, sun)
    

# professor não entendi pq vc pediu pra haver pelo menos duas funções: uma para fazer a conversão e uma para a saída.

#qual a necessidade de colocar outra função?

#tambem não fiz a parte "Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M."



while True:
    resp = input('\nHora atual [hh:mm] (0 para parar)\nR: ').strip().replace(':', ' ').split()
    if resp[0] == '0':
        break
    try:
        h = int(resp[0])
        m = int(resp[1])
        if h > 24 or h < 0 or m >= 60 or m < 0:
            print('Insira um horário válido')
        else:
            print(convert(h, m))
    except:
        print('Insira um horário válido')