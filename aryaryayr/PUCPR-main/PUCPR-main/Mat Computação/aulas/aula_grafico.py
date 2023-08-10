import matplotlib.pyplot as plt
import numpy as np

# f(x) = 2x + 1
def f(x):
    return 2*x + 1

vx = np.arange(-10,10,0.1)
vy = []

for x in vx:
    y = f(x)
    vy.append(y)

fig = plt.figure(figsize=(7,7))

plt.plot(vx, vy, label = 'f(x) = 2x + 1', color = 'g')
plt.title('f(x) = 2x + 1')
plt.xlabel('Eixo X')
plt.ylabel('Eixo y')
plt.show()