import numpy as np
import matplotlib.pyplot as plt

def func(x, a, b):
    fn = a*np.exp(x) + b*np.exp(-x)
    return fn

x = np.linspace(-6, 6)
fn1 = func(x, 2, 3)
fn2 = func(x, 4, 6)

plt.plot(x, fn1)
plt.plot(x, fn2)

p2_1 = np.polyfit(x,fn1,2)
p3_1 = np.polyfit(x,fn1,3)
p4_1 = np.polyfit(x,fn1,4)

p2_2 = np.polyfit(x,fn2,2)
p3_2 = np.polyfit(x,fn2,3)
p4_2 = np.polyfit(x,fn2,4)

plt.legend(('fn1', 'fn2'))
plt.title('ae^x + be^-x')
plt.xlabel('x')
plt.ylabel('y')
plt.savefig("A2 Q1.png")
plt.show()



# plt.plot(x, fn1)
# plt.plot(x, np.polyval(p2_1,x))
# plt.plot(x, np.polyval(p3_1,x))
# plt.plot(x, np.polyval(p4_1,x))

# plt.legend(('fn1', 'p2', 'p3', 'p4'))
# plt.title('ae^x + be^-x')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.savefig("A2 Q1 - a.png")
# plt.show()

# plt.plot(x, fn2)
# plt.plot(x, np.polyval(p2_2,x))
# plt.plot(x, np.polyval(p3_2,x))
# plt.plot(x, np.polyval(p4_2,x))

# plt.legend(('fn2', 'p2', 'p3', 'p4'))
# plt.title('ae^x + be^-x')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.savefig("A2 Q1 - b.png")
# plt.show()



