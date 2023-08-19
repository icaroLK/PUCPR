
# alternar = True
# for oi in range(1, 8+1):
#     if alternar:
#         print("V")
#     else:
#         print("F")
#     if oi % 2 == 0:
#         alternar = not alternar





def verseeh(posletra, linha):
    global alternar
    if posletra == 0:
        passo = QtdLinhas/2


    elif posletra == 1:
        passo = 2

    elif posletra == 2:
        passo = 1

    if (linha-1) % passo == 0:
        alternar = 1
        return 'V'
    else:
        alternar = 0
        return 'F'



def cu(X, linha):
    global alternar
    if X == 0:
        passo = 4

    elif X == 1:
        passo = 2

    elif X == 2:
        passo = 1
    
    if linha % passo == 0:
        return 'V'
    else:
        return 'F'