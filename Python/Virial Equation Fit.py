# Program to calculate fugacity for Q3 A4
import numpy as np
import matplotlib.pyplot as plt

Z = [0.9960, 0.9838, 0.9714, 0.9588, 0.8202, 0.6417]
P = [1.01, 4.05, 7.09, 10.1, 40.5, 71.0]

B = np.polyfit(P, Z, 2)
print('coeffs: ', B)
Z1 = np.polyval(B, P)
print('Z from fitted eqn:', Z1)

plt.scatter(P, Z)
plt.plot(P, Z1)
plt.legend(('Fitted Values', 'Given data'))
plt.title('Virial Equation Fit')
plt.xlabel('P')
plt.ylabel('Z')
plt.show()

f = Z1*P
fg = np.multiply(Z, P)  #fg is calculated using given data
print('f from fitted eqn: ', f)
print('f from given values: ', fg)

print('Making C coeff 1:', 'B3:', B[0]/B[2], 'B2:', B[1]/B[2])
