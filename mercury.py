
import numpy as np


rMR0 = 4.60 # la distancia M - S inicial
vMR0 = 5.10e-1 # velocidad inicial de MR
c_a = 9.90e-1 # el factor que multiplica a la acelaración

TMR = 8.80e+1 #periodo de la órbita de mercurio
rS = 2.95e-7 # radio de Sw del sol
rL2 = 8.19e-7 # momento angular de mercutoi

MRelX = [0]
MRelY = [rMR0]

MRelR = np.array([MRelX[0], MRelY[0]]) #pos. inicial de M
MRelV = np.array([vMR0, 0]) #vel.inicial de M

#creeamos una version no relativista:
Mx = [0]
My = [rMR0]
Mr = np.array([MRelX[0], MRelY[0]]) #pos. inicial de M
Mv = np.array([vMR0, 0]) #vel.inicial de M



Sx = [0]    #coordenadas del sol
Sy = [0]


# Definition of the time step
dt = 2 * vMR0 / c_a / 20

def module(vec):
    return (vec[0]**2 + vec[1]**2)**0.5

def computeDistance(pl1, pl2):
    d = ((pl2[1]-pl1[1])**2 + (pl2[0]-pl1[0])**2)**0.5
    return d



def updateCoord(Rold, Vold, alpha=0, beta=0):
    modRold = module(Rold)

    temp = 1 + alpha * rS / modRold + beta * rL2 / modRold**2
    aMs = c_a * temp / modRold**2

    vec_aMS = -aMs * (Rold / modRold)

    Vnew = Vold + vec_aMS * dt

    Rnew = Rold + Vnew * dt
    return Rnew, Vnew


t = 0.0
alpha = 0
beta = 3e5
distPrev = 0
dist = 0
r0 = dt * 10
# Execute the loop as long as t < 2*TM
while t < 2*TMR:
    # Set the frame rate (you can choose a higher rate to accelerate the program)
    #rate(100)
    # Update the drawn trajectory with the current position
    #M.trajectory.append(pos=M.pos)
    # Update velocity and position
    MRelR, MRelV = updateCoord(MRelR,  MRelV , alpha, beta)
    Mr, Mv = updateCoord(Mr,  Mv)
    
    MRelX.append(MRelR[0])
    MRelY.append(MRelR[1])

    Mx.append(Mr[0])
    My.append(Mr[1])   
    
    distRel = computeDistance([Sx, Sy], [MRelX[-1], MRelY[-1]])
    distNRel = computeDistance([Sx, Sy], [Mx[-1], My[-1]])
    #if distRel < r0 or distNRel < r0:
    #    break
    '''
    print(dist, distPrev)
    distPrev = dist
    acerc = False
    if dist < distPrev: #si la distancia está bajando (se acerca al perih)
        acerc = True
        #print("se acerca")

    if dist > distPrev: print("se aleja!")

    if acerc == True and dist > distPrev:
        print(np.arccos(Mx[-1]/dist))

    #print(Mr[0], Mr[1])
    '''
    # Advance time by one step
    t = t + dt


import matplotlib.pyplot as plt
plt.plot(MRelX, MRelY, '.')
plt.plot(Mx, My, '.')
plt.axis("equal")
plt.scatter(Sx[0], Sy[0])
plt.show()