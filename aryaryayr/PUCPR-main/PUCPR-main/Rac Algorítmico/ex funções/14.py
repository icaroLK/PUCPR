from itertools import permutations
import os

def verificar(q):
    s = q[0] + q[1] + q[2]
    if (q[3] + q[4] + q[5] != s or
        q[6] + q[7] + q[8] != s or
        q[0] + q[3] + q[6] != s or
        q[1] + q[4] + q[7] != s or
        q[2] + q[5] + q[8] != s or
        q[0] + q[4] + q[8] != s or
        q[2] + q[4] + q[6] != s):
        return False
    return True


def mostrar(q):
    for c in range(0, 9, 3):
        print(q[c], q[c+1], q[c+2])
    print()

os.system('cls')
n = list(range(1,10))
comb = permutations(n)
count = 1
for c in comb:
    if verificar(c):
        print(f'\033[1;36m{count}º quadrado:\033[m')
        count += 1 
        mostrar(c)
