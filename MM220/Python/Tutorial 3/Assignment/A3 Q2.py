import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

# Modifying file values from lattice parameter (a) to Volume (a^3)
file = open("lat.dat", "r")
mod_file = open("latmod.dat", "w")
data = []
while True:
    line = file.readline()
    if line:
        data.append(list(map(float, line.split()[0:])))
    if not line:
        break
file.close()

for i in range(len(data)):
    mod_file.write('%6.6f %6.6f \n' %((data[i][0])**3, data[i][1]))
mod_file.close()

# Storing Volume and Energy data in separate lists
Vdata = []
Edata = []
for i in range(len(data)):
    Vdata.append((data[i][0])**3)
    Edata.append(data[i][1])

# Fitting V and E data to a second order polynomial to find initial parameters
p2 = np.polyfit(Vdata, Edata, 2)
Efit = np.polyval(p2, Vdata)

# Storing coefficients in a, b, c
a = p2[0]
b = p2[1]
c = p2[2]

# Calculating initial parameter values
# E = aV^2 + bV + c
# dE/dV = 2aV + b
# d2E/dV2 = 2a
# dE/dV = 0 at equillibrium
# B'0 (B_0) is usually a small number 

V0 = -b/(2*a)
E0 = a*V0**2 + b*V0 + c
B0 = 2*a*V0
B_0 = 4

print(V0, '\n', E0, '\n', B0, '\n', B_0)

# Plotting Fitted and Original data 
plt.scatter(Vdata, Edata, c = 'k', s = 9)
plt.plot(Vdata, Efit)
plt.legend(('Fitted Data', 'Original Data'))
plt.xlabel('Volume')
plt.ylabel('Internal Energy')
plt.title('Original and Fitted Data')
plt.savefig('A3 Q2 - a.png')
plt.show()

# Defining the BM EOS function
def func(Vdata, V0, E0, B0, B_0):
    k = ((V0/Vdata)**(2.0/3.0))
    A = B_0*((k - 1)**3)
    B = ((k - 1)**2)*(6 - 4*k)
    return E0 + (9*V0*B0/16)*(A + B)

# Optimizing Parameters
E = func(Vdata, V0, E0, B0, B_0)
# E_list = list(E)
popt, pconv = opt.curve_fit(func, Vdata, E)
# print(popt)

# Plotting BM EOS data
plt.plot(Vdata, func(Vdata, *popt))
plt.title('Plot of Optimized BM EOS')
plt.xlabel('Volume')
plt.ylabel('Internal Energy')
plt.savefig('A3 Q2 - b.png')
plt.show()

# Printing Optimized Parameters
print('V0: ', popt[0])
print('E0: ', popt[1])
print('B0: ', popt[2])
print('B_0: ', popt[3])
