# def div(a, tam):
#     ready = []
#     sub = []
#     for c in a:
#         sub.append(c)
#         if len(sub) == tam:
#             ready.append(sub)
#             sub = []
#     return ready

m = []
sub = []
final = []

resp = int(input('Insira o tamanho da matriz: '))

count = 0


for l in range(resp):
    for c in range(resp):
        if c == l:
            m.append(1)
        else:
            m.append(0)

for c in m:
    sub.append(c)
    if len(sub) == resp:
        final.append(sub)
        sub = []


for c in final:
    print(c)


#print('{}\n{}\n{}'.format(final[0], final[1], final[2]))

#print(div(m, resp))