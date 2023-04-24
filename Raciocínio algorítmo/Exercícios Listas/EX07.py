nums = [3,11,6,32,15,22,4,10,5]
sub = []
fim = []

org = sorted(nums, reverse=True)

for i,v in enumerate(org):
    sub.append(v)
    if len(sub) == 3:
        fim.append(sub)
        sub = []


# for c in fim:
#     print(c)
    

for l in range(3):
    for c in range(3):
        print('[ {:2d} ]'.format(fim[l][c]), end=' ')
    print()