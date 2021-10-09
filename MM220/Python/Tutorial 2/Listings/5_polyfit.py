import matplotlib.pyplot as plt
import numpy as np

def func(x, a, b, c):
    return a * np.exp(-b * x) + c

xdata = np.linspace(0, 4, 50)
y = func(xdata, 2.5, 1.3, 0.5)
y_noise = 0.2 * np.random.normal(size=xdata.size)
ydata = y + y_noise

plt.scatter(xdata, ydata)

p1 = np.polyfit(xdata,ydata,1)
print(p1, np.poly1d(p1))
p2 = np.polyfit(xdata,ydata,2)
p3 = np.polyfit(xdata,ydata,3)

plt.plot(xdata, np.polyval(p1,xdata), 'r-')
plt.plot(xdata, np.polyval(p2,xdata), 'b-')
plt.plot(xdata, np.polyval(p3,xdata), 'g-')

plt.xlabel("x")
plt.ylabel("y")
plt.legend(('p_1', 'p_2', 'p_3', 'data'))
plt.title('Polynomial Fitting')
plt.savefig("polyfit.png")
plt.show()
