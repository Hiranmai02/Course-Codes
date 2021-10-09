import numpy as np
from matplotlib.pylab import plt 

class projectile:
    def __init__(self, angle, v0, time):
            self.t = np.linspace(0, time, 300)
            self.dt = self.t[1] - self.t[0]
            self.g = 9.8
            self.m = 1

            self.v0 = v0
            self.vx = v0*np.cos(angle)
            self.vy = v0*np.sin(angle)
            self.y0 = 0
            self.x0 = 0
            self.y_list = [self.y0]
            self.x_list = [self.x0]
            self.vxl = [self.vx]
            self.vyl = [self.vy]
            self.Cd = 0.005
            
    
    def dist(self):
            for i in range(1, len(self.t)):
                self.v = np.sqrt(self.vx*self.vx + self.vy*self.vy)
                self.Fd = self.Cd*self.v*self.v
                self.alpha = np.arctan(self.vy/self.vx)
                self.ax = (-self.Fd*np.cos(self.alpha))/self.m
                self.ay = -self.g - (self.Fd/self.m)*np.sin(self.alpha)

                self.vy += self.ay*self.dt
                self.y0 += self.vy*self.dt + 0.5*self.ay*self.dt ** 2 
                self.vx += self.ax*self.dt
                self.x0 += self.vx*self.dt + 0.5*self.ax*self.dt ** 2

                if self.y0 > 0:
                    self.y_list.append(self.y0)
                    self.x_list.append(self.x0)
                    self.vyl.append(self.vy)
                    self.vxl.append(self.vx)
                else:
                    self.t1 = self.t[0:i]
                    break

            return self.x_list, self.y_list, self.vxl, self.vyl, self.t1
    
    def plot(self):
        plt.plot(self.x_list, self.y_list)
        plt.xlabel("x")
        plt.ylabel("y")
        plt.show()

        plt.plot(self.t1, self.vxl)
        plt.xlabel("t")
        plt.ylabel("vx")
        plt.show()

        plt.plot(self.t1, self.vyl)
        plt.xlabel("t")
        plt.ylabel("vy")
        plt.show() 

p1 = projectile(np.pi/3, 30, 30)
x_list1, y_list1, vx1, vy1, t1 = p1.dist()
range1 = x_list1[-1] - x_list1[0]
print("Range:", range1)
p1.plot()
