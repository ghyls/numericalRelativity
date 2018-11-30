

G = 6.67408e-11
G = 1
dt = 0.001
rmin = 10 * dt
t0 = 0

class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.mass = mass
        self.xtray = []
        self.ytray = []

sun = Planet(0, 0, 50)


earth = Planet(10, 0, 5)

earth.vx = 1
earth.vy = 1

def computeDistance(pl1, pl2):
    d = ((pl2.y-pl1.y)**2 + (pl2.x-pl1.x)**2)**0.5
    return d

def updateCoord(pl1, pl2, r):
    F =  G * pl1.mass * pl2.mass / r**2
    Fx = F * (pl2.x-pl1.x) / r
    Fy = F * (pl2.y-pl1.y) / r
    
    pl1.vx += Fx / pl1.mass * dt
    pl1.vy += Fy / pl1.mass * dt
    pl2.vx += -Fx / pl2.mass * dt
    pl2.vy += -Fy / pl2.mass * dt

    pl1.x += pl1.vx * dt
    pl1.y += pl1.vy * dt
    pl2.x += pl2.vx * dt
    pl2.y += pl2.vy * dt
    
    #print(pl1.vx, r)

t = t0
while t < 50:
    r = computeDistance(earth, sun)
    if r < rmin: break
    earth.xtray.append(earth.x)
    earth.ytray.append(earth.y)
    sun.xtray.append(sun.x)
    sun.ytray.append(sun.y)
    updateCoord(earth, sun, r)
    t += dt

#print(earth.xtray)
#print(earth.ytray)


import matplotlib.pyplot as plt
plt.plot(earth.xtray, earth.ytray)
plt.plot(sun.xtray, sun.ytray)
plt.scatter(sun.x, sun.y)
plt.show()
