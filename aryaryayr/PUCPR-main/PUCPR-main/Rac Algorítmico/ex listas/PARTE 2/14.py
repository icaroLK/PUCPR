qst = ["Telefonou para a vítima?", "Esteve no local do crime?", 
"Mora perto da vítima?", "Devia para a vítima?", "Já trabalhou com a vítima?"]
yes = []

for c in range(5):
    ans = str(input(f'{qst[c]}: ')).strip().upper()[0]
    if ans in 'S':
        yes.append(1)

if len(yes) == 2:
    print('Você é \033[1;33mSUSPEITO!\033[m')
elif 3 <= len(yes) <= 4:
    print('Você é \033[1;35mCÚMPLICE!\033[m')
elif len(yes) == 5:
    print('Você é o \033[1;31mASSASSINO!\033[m')
else:
    print('Você está \033[1;32mliberado.\033[m')