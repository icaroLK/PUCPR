nums = [3, 11, 6, 32, 15, 22, 4, 10, 5]
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
nums.sort(reverse=True)
pos = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = nums[pos]
        pos += 1

for l in range(0, 3):
    print('|', end='')
    for c in range(0, 3):
        print(f'{matriz[l][c]:^5}', end='')
    print('|')
