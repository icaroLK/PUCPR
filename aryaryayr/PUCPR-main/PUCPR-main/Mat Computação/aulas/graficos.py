import matplotlib.pyplot as plt
import numpy as np

# crescente = a > 1
# decrescente = 0 > a > 1
# inexstente a < 0

# f(x) = 4**x
a = float(input('Digite o a: '))
def f(x, a):
    y = a**x
    return y

vx = np.arange(-10, 10, 0.1)
vy = []

for x in vx:
    y = f(x,a)
    vy.append(y)

fig =  plt.figure(figsize=(7,7))

plt.plot(vx, vy, label = 'f(x) = a**x', color = 'g')
plt.title(f'f(x) = {a}**x')
plt.xlabel('Eixo x')
plt.ylabel('Eixo y')
plt.show()