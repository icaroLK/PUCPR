# (p -> (q -> p))
# (p→(q→p))
# (F→(V→F))

# (F→(V→F))

def implicacao(a, b):
    if a == 'V' and b == 'V' or a == 'F' and b == 'V' or a == 'F' and b == 'F':
        return 'V'
    elif a == 'V' and b == 'F':
        return 'F'



def confParent(analise):
    alt = False
    cont = []
    for carac in analise:

        if carac == '(':
            alt = True
            cont.append(carac)
        elif carac == ')':
            alt = False              ########################################## aqui
            if cont[-1] != ')':
                cont.append(carac)

        if alt == True:
            if carac not in ('(', ')'):
                cont.append(carac)

            elif carac == '(':
                cont = []
                cont.append(carac)
    return cont






def listamenoslista(lista1, lista2, conf):
    result = []
    i = 0
    cu = 0

    while i < len(lista1):
        if lista1[i:i + len(lista2)] == lista2:
            cu = i
            i += len(lista2)
        else:
            result.append(lista1[i])
            i += 1

    result.insert(cu, implicacao(confParent(conf)[1], confParent(conf)[-2]))
    return result







exp = input("Insira a expressão: ")
listaInput = []
for letra in exp:
    listaInput.append(letra)
#print(listaInput)


#print(confParent())

#print(implicacao(confParent(exp)[1], confParent(exp)[-2]))

#print(listamenoslista(listaInput, confParent(exp), exp))


lista = listamenoslista(listaInput, confParent(exp), exp)






count = 0
while len(lista) > 1:
    print('aa')
    lista = implicacao(confParent(lista)[1], confParent(lista)[-2])

    count += 1
    if count == 20:
        break

print('\n\n')
print(f'{exp} = {lista}')








'''
--------------VERSAO SEM PARENTESES--------------
def confParent():
    alt = False
    cont = []
    for carac in exp:
        if carac == '(':
            alt = True
        elif carac == ')':
            alt == False
        
        if alt == True:
            if carac not in ('(', ')'):
                cont.append(carac)
            elif carac == '(':
                cont = []
    return cont


--------------VERSAO COM PARENTESES--------------
def confParent():
alt = False
cont = []
for carac in exp:

    if carac == '(':
        alt = True
        cont.append(carac)
    elif carac == ')':
        alt == False
        if cont[-1] != ')':
            cont.append(carac)


    if alt == True:
        if carac not in ('(', ')'):
            cont.append(carac)

        elif carac == '(':
            cont = []
            cont.append(carac)
return cont

'''