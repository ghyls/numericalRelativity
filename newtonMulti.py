import random as rn
import sys
rn.seed(39)


G = 1
dt = 0.0002
tmax = 10
t0 = 0

nObj = 3   #number of objects in the simulation


allX = []
allY = []

allVx = []
allVy = []

allM = []

status = []

for i in range(nObj):   #rellenar valores iniciales
    allX.append(rn.random()*20)
    allY.append(rn.random()*20)


    allVx.append((rn.random()-0.5))
    allVy.append((rn.random()-0.5))

    #allM.append(rn.random()*20)
    allM.append(3)

    status.append(1)

print(sum(allVx)/nObj)
print(sum(allVy)/nObj)



#allM = [3, 3, 3, 3, 3, 3]


allM = [3, 3, 3] 
allX = [1, 10, 15]
allY = [1, 0, 5]


allVx = [0, -1, -1]
allVy = [0, 0, 0]


def computeDistance(x1, y1, x2, y2):
    d = ((y2-y1)**2 + (x2-x1)**2)**0.5

    return d

def updateCoord():
    #print("hello!", nObj)
    RMIN = [elem**0.3/8 for elem in allM]
    for i in range(nObj):
        for j in range(nObj):
            #print(status[i], status[j] )
            global status
            if j < i and status[j] == 1 and status[i] == 1:
                #print("no hell")
                #print(i, j)
                r = computeDistance(allX[i], allY[i], allX[j], allY[j])
                #print("distance, ", r)
                rmin = max(RMIN[j], RMIN[i])
                if r < rmin:
                    print("=======================================")
                    #print(i, j)
                    print(allM[i], allM[j])

                    print("un choque: ", i, j)
                    print(allX[i], allX[j])
                    print(allY[i], allY[j])

                    allM[i] += allM[j]
                    allVx[i] += allVx[j]
                    allVy[i] += allVy[j]

                    status[j] = 0

                                    

                F =  G * allM[i] * allM[j] / r**2
                Fx = F * (allX[j]-allX[i]) / r
                Fy = F * (allY[j]-allY[i]) / r


                allVx[i] += Fx / allM[i] * dt
                allVy[i] += Fy / allM[i] * dt
                allVx[j] += -Fx / allM[j] * dt
                allVy[j] += -Fy / allM[j] * dt
                
                allX[i] = (allX[i] + allVx[i] * dt)
                allY[i] = (allY[i] + allVy[i] * dt)
                allX[j] = (allX[j] + allVx[j] * dt)
                allY[j] = (allY[j] + allVy[j] * dt)
                
                lim=20
                if allX[i] > lim: allX[i] -= lim
                elif allX[i] < 0: allX[i] += lim
                if allY[i] > lim: allY[i] -= lim
                elif allY[i] < 0: allY[i] += lim
                if allX[j] > lim: allX[j] -= lim
                elif allX[j] < 0: allX[j] += lim
                if allY[j] > lim: allY[j] -= lim
                elif allY[j] < 0: allY[j] += lim
                

                    


                    



t = t0

f = open("data.txt", "w")
xFinalTemp = [[]]*nObj
yFinalTemp = [[]]*nObj
while t <= 10:
    updateCoord()
    
    A = []
    A.append(t)                                         #tiempo

    for j in range(nObj):
        if allX[j] != xFinalTemp[j] and allY[j] != yFinalTemp[j]:
            A.append(allM[j])                           #masa
            A.append(allX[j])
            A.append(allY[j])
            xFinalTemp[j] = allX[j]
            yFinalTemp[j] = allY[j]
            print(xFinalTemp)
        else:
            pass
    for elem in A:
        f.write(str(elem) + " ")
    f.write('\n')

    sys.exit()
    t += dt


'''
import matplotlib.pyplot as plt

#print(len(allXFinal))
#print(len(allXFinal[0]))
#print(len(allXFinal[1]))
#print(len(allXFinal[2]))


for i in range(nObj0):
    xCoord = allXFinal[i]   
    yCoord = allYFinal[i] 
    plt.scatter(allXFinal[i][0], allYFinal[i][0])
    plt.plot(xCoord, yCoord, '.', markersize=1)
'''

'''

for i in range(len(allXFinal[0])):
    plt.scatter(allXFinal[0][i], allYFinal[0][i])
    plt.scatter(allXFinal[1][i], allYFinal[1][i])
    plt.scatter(allXFinal[2][i], allYFinal[2][i])
    plt.pause(0.0001)


plt.axis('equal')

plt.show()
'''

     




