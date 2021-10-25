import random
import numpy as np
import math
import matplotlib.pyplot as plt

n = 10000
sq = 0
cir = 0
x = []
y = []

def dist(x, y):
    return np.sqrt(x**2 + y**2)

for i in range(n):
    x.append(random.uniform(-1,1)) 
    y.append(random.uniform(-1,1))

    if dist(x[i], y[i]) < 1:
        plt.plot(x[i], y[i], 'r.', markersize = 3)
        cir += 1
    else:
        plt.plot(x[i], y[i], 'b.', markersize = 3)
        sq += 1

pt = cir + sq
pi = 4*(cir/pt)
print(pi)
print(math.pi - pi)

plt.axis([-1,1,-1,1])
plt.title('Monte Carlo Simulation for pi')
plt.show()
