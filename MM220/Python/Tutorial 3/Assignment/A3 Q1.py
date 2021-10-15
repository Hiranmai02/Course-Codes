import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

def func(x):
    x = sp.symbols('x')
    return x*sp.exp(x)

def integrate(x):
    x = sp.symbols('x')
    val = sp.integrate(func(x), x)
    return val

x = sp.symbols("x")
value = integrate(x)
print (value)

x = sp.symbols('x')
intx = []
fx = []

for i in np.linspace(0,3):
    intx.append(value.evalf(subs = {x: i}))

for i in np.linspace(0,3):
    fx.append(func(x).evalf(subs = {x: i}))

x = np.linspace(0,3)
plt.plot(x,fx)
plt.plot(x,intx)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(('f(x)', 'int(f(x))' ))
plt.savefig('A3 Q1.png')
plt.show()


    