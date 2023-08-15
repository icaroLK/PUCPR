from random import choice

mat = [0] * 9 
qtd = 1
while True:
    num = [1,2,3,4,5,6,7,8,9]
    for coun in range(9):
        mat[coun] = choice(num)
        num.remove(mat[coun])


                # [a] [b] [c]
                # [d] [e] [f]
                # [g] [h] [i]

    a = mat[0]
    b = mat[1]
    c = mat[2]
    d = mat[3]
    e = mat[4]
    f = mat[5]
    g = mat[6] 
    h = mat[7]
    i = mat[8]

    # if mat[0] + mat[1] + mat[2] == mat[0] + mat[3] + mat[6] == mat[0] + mat[4] + mat[8]:
    #     break
    # esse jeito aqui eu achei q um quadrado mágico era a soma de (a + d + g == a + b + c == a + e + i) mas aparentemente tava errado ent esse novo código faz com que a soma de todos as linhas e todas as colunas sejam iguais (mas fica com MUITO mais tentativas)


    if a + b + c == d + e + f == g + h + i == a + d + g == b + e + h == c + f + i == a + e + i == c + e + g:
        break
    qtd += 1
print('\nForam necessários {} tentativas\n'.format(qtd))
for oi in range(9):
    print(mat[oi], end=' ')
    if oi == 2 or oi == 5:
        print()
print('\n')



































####   REPETINDO OS NÚMEROS   ####


# from random import randint, choice

# num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# mat = [0] * 9

# penes = 1

# while True:
#     for c in range(9):
#         mat[c] = choice(num)
# #    print(mat)

#     if mat[0] + mat[1] + mat[2] == mat[0] + mat[3] + mat[6] == mat[0] + mat[4] + mat[8]:
#      #   print(mat)
#         break

#     penes += 1
# print('\nForam necessários {} tentativas\n'.format(penes))

# for c in range(9):
#     print(mat[c], end=' ')
#     if c == 2 or c == 5:
#         print()

# print('\n')


