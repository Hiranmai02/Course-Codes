import matplotlib.pyplot as plt
import numpy as np

def func_duo(x):
    return np.sin(x) , np.cos(x)

def comp_func(x, a, b):
    return a*np.sin(x) + b*np.cos(x)

xdata = np.linspace(-np.pi, np.pi, 300)
sin, cos = func_duo(xdata)
y_comp = comp_func(xdata, 2, 1)

plt.plot(xdata, sin, ".", label="sin")
plt.plot(xdata, cos, ".", label="cos")
plt.plot(xdata, y_comp, ".", label="Data")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Harmonics")
plt.legend(( 'sin(x)', 'cos(x)','harmonics(x)'))

plt.savefig('harmonics.png')
plt.show()