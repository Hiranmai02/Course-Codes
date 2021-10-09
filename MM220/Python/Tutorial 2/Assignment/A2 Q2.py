import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.core.symbol import Symbol

def LJ(r, A, B):
    V = (B/(r**12)) - (A/(r**6))
    return V

# Conversion of V to eV (Standard)
# A = (1.024/1.6)*(10**-4)
# B = (1.582/1.6)*(10**-7)

# A and B here are divided by the Boltzmann Constant
A = 1.024/1.381
B = (1.582/1.381)*(10**-3)
r = np.linspace(0.3, 0.8)
V = LJ(r, A, B)
plt.plot(r, V)
plt.xlabel('r')
plt.ylabel('V(r)')
plt.title('LJ Potential')
plt.savefig('A2 Q2 - a')
plt.show()

def force(r, A, B):
    r = sp.symbols('r')
    V = (B/(r**12)) - (A/(r**6))
    F = sp.diff(V, r)
    return F, V

r = sp.symbols('r')
F_1, V_1 = force(r, A, B)

V1 = []
F1 = []

for i in np.linspace(0.3, 0.8):
    V1.append(V_1.evalf(subs={r: i}))
    F1.append(F_1.evalf(subs={r: i}))

for i in range(len(F1)):
    F1[i] = -1*F1[i]

r = np.linspace(0.3, 0.8)
plt.plot(r, F1)
plt.xlabel('r')
plt.ylabel('F(r)')
plt.title('LJ Force')
plt.savefig('A2 Q2 - b')
plt.show()

def minF(f):
    r = Symbol('r')
    rmin = sp.solve(f, r)
    return rmin

rm = minF(F_1)
for i in range(len(rm)):
    if rm[i] > 0:
        realrm = rm[i]
        break
print('r0:', realrm)