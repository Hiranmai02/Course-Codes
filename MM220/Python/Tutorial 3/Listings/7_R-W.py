import numpy as np
import matplotlib.pyplot as plt

file = open("lat.dat", "r")
mod_file = open("modlat.dat", "w")
data = []
while True:
    line = file.readline()
    if line:
        data.append(list(map(float, line.split()[0:])))
    if not line:
        break

file.close()
print (data[0][0], data[0][1])

for i in range(len(data)):
    mod_file.write('%6.6f %6.6f \n' %(data[i][0], data[i][1]))

mod_file.close()

x, y = np.loadtxt('lat.dat', delimiter=None, unpack=True)
print (x[0],y[0])

plt.xlabel("lattice_parameter (A)")
plt.ylabel("Energy (eV)")
plt.plot(x,y, label='Loaded from file!')
plt.savefig('latenergy.png')
plt.show()