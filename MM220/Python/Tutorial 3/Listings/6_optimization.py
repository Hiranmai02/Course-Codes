import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise
plt.plot(xdata, ydata, ".", label="Data")
popt, pconv = opt.curve_fit(func, xdata, ydata)
print (popt)

plt.plot(xdata, func(xdata, *popt), label="fit")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(('data', 'opt_plot' ))
# plt.savefig('opt.png')
plt.show()

