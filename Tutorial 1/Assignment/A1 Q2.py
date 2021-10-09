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
    y_list = [y0]
    x_list = [x0]
    vxl = [vx]
    vyl = [vy]

    Cd = 0.005

    for i in range(1, len(t)):
        
        v = np.sqrt(vx*vx + vy*vy)
        Fd = Cd*v*v
        alpha = np.arctan(vy/vx)
        ax = (-Fd*np.cos(alpha))/m
        ay = -g - (Fd/m)*np.sin(alpha)

        vy += ay*dt
        y0 += vy*dt # + 0.5*ay*dt*dt
        vx += ax*dt
        x0 += vx*dt # + 0.5*ax*dt*dt

        if y0 > 0:
            y_list.append(y0)
            x_list.append(x0)
            vyl.append(vy)
            vxl.append(vx)

        else:
            t1 = t[0:i]
            break
            
    return x_list, y_list, vxl, vyl, t1

x_list1, y_list1, vxl1, vyl1, t1 = projectile(np.pi/3, 30, 30)
range1 = x_list1[-1] - x_list1[0]
print("Range:", range1)

# print(x_list1, y_list1)
plt.plot(x_list1, y_list1)
plt.xlabel("x")
plt.ylabel("y")
plt.show()

plt.plot(t1, vxl1)
plt.xlabel("t")
plt.ylabel("vx")
plt.show()

plt.plot(t1, vyl1)
plt.xlabel("t")
plt.ylabel("vy")
plt.show() 
