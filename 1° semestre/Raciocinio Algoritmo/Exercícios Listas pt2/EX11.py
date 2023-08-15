a = [1,2,3,4,5]
b = ['a', 'b', 'c', 'd', 'e']
k = ['@', '#', '$', '%', '&', '*']
new = []

for c in a:
    new.append(c)

cu = 1
aaa = 2
for c in range(len(b)):
    new.insert(cu, b[c])
    cu += 2

for c in range(len(k)):
    new.insert(aaa, k[c])
    aaa += 3

print(new)

