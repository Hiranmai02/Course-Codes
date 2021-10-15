import numpy as np
import matplotlib.pyplot as plt

v = np.array([13.72, 14.83, 16.0, 17.23, 18.52])
e = np.array([-56.29, -56.41, -56.46, -56.46, -56.42])
print (v.shape, e.shape)

a = np.polyfit(v,e,2)
print(a)
plt.plot(v,e)
vfit = np.linspace(min(v),max(v),100)

plt.plot(vfit, (a[0]*vfit**2 + a[1]*vfit + a[2]))
plt.legend(('original', 'parabolic fit'))
plt.xlabel("Volume ($\AA^3$)")
plt.ylabel("Energy (eV)")
plt.savefig('eos.png')
plt.show()
