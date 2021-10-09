import numpy as np
from matplotlib.pylab import plt 

def projectile(angle, v0, time):
    t = np.linspace(0, time, 300)
    dt = t[1] - t[0]
    g = 9.8
    m = 1

    v0 = v0
    vx = v0*np.cos(angle)
    vy = v0*np.sin(angle)
    y0 = 0
    x0 = 0
    vg = 0
    y_list = [y0]
    x_list = [x0]
    ax = 0
    ay = -g

    for i in range(1, len(t)):
        vg += ay*dt
        y0 += (vg + vy)*dt
        x0 += vx*dt

        if y0 > 0:
            y_list.append(y0)
            x_list.append(x0)
        else:
            break

    return x_list, y_list

x_list1, y_list1 = projectile(np.pi/4, 60, 25)
range = x_list1[-1] - x_list1[0]
print("Range", range)
# print(x_list1, y_list1)
plt.plot(x_list1, y_list1)
plt.xlabel("x")
plt.ylabel("y")
plt.show()
