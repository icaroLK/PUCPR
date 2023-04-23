m1 = [[1,2,3], [4,5,6], [7,8,9]]

m2 = [[3,2,3], [1,3,3], [0,2,2]]

m3 = []

mf1 = []
mf2 = []
mf3 = []


s = 0





for l in range(3):
    for c in range(3):
        s = m1[l][c] + m2[l][c]
        if l == 0:
            mf1.append(s)
        if l == 1:
            mf2.append(s)        
        if l == 2:
            mf3.append(s)

m3.extend([mf1, mf2, mf3]) # esse extend faz a mesma coisa que 3 chamada de append


print(m3)
