a = [1,2,3,4,5]
b = ['a', 'b', 'c', 'd', 'e']
new = []

for c in a:
    new.append(c)

cu = 1

for c in range(len(b)):
    new.insert(cu, b[c])
    cu += 2
print(new)