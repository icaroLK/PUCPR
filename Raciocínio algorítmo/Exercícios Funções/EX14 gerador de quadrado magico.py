from random import randint, choice

mat = [0] * 9 

qtd = 1

while True:
    num = [1,2,3,4,5,6,7,8,9]
    for c in range(9):
        mat[c] = choice(num)
        num.remove(mat[c])

#    print(mat)

    if mat[0] + mat[1] + mat[2] == mat[0] + mat[3] + mat[6] == mat[0] + mat[4] + mat[8]:
     #   print(mat)
        break


    qtd += 1
print('\nForam necessários {} tentativas\n'.format(qtd))

for c in range(9):
    print(mat[c], end=' ')
    if c == 2 or c == 5:
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


