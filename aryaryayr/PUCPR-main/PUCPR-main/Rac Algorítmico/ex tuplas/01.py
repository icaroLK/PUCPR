cadastro = []

while True:
    nome = str(input('Nome: ')).title()
    RG = input('RG: ').replace('.','').replace('-','')
    CPF = input('CPF: ').replace('.','').replace('-','')
    RGf = f'{RG[:2]}.{RG[2:5]}.{RG[5:8]}-{RG[8:]}'
    CPFf = f'{CPF[:3]}.{CPF[3:6]}.{CPF[6:9]}-{CPF[9:]}'
    pessoa = (nome, RGf, CPFf)
    cadastro.append(pessoa)
    ans = str(input('deseja continuar? ')).strip().upper()[0]
    if ans in 'N':
        break

for pessoa in cadastro:
    print(f'{pessoa[0]}  -  {pessoa[1]}  -  {pessoa[2]}')
