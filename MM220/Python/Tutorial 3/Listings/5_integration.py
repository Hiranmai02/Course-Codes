import scipy
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
import sympy

def func(x):
    return 4*x**2 +2

def int_func(a, b):
    I = quad(func, a , b)
    return I[0]

print(int_func(0, 2))

def int(x):
    x = sympy.symbols('x')
    val =sympy.integrate(func(x), x)
    return val

x = sympy.symbols("x")
value = int(x)
print (value)

x = sympy.symbols('x')
intx=[]

for i in np.linspace(-3,3):
    intx.append(int(x).evalf(subs={x: i}))

x = np.linspace(-3,3)
plt.plot(x,func(x))
plt.plot(x,intx)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(('f(x)', 'int(f(x))' ))
plt.savefig('int.png')
plt.show()