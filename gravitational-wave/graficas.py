import matplotlib.pyplot as plt 
import numpy as np

datos = np.loadtxt('COMP/Phi_2.x')  #recordar tener cuidado con la ubicacion del 'Phi_2.x'
xmin = min(datos[:,0])
xmax = max(datos[:,0])

index = np.where(datos == xmax)[0]   #conozco el inicio (o el final) de cada bloque, me devuelve la posicion en datos[]
                                     #de cada elemento fin de bloque
n = len(index)                       #la longitud de este array me dara el numero total de bloques (imagenes)

imagenes = np.split(ary=datos, indices_or_sections=n, axis=0) #divido datos en cada uno de los bloques (imagenes)
                                                              #axis=0 separa por filas (cada pareja de datos es una fila)
                                                              #imagenes[i] me dara la imagen en t=ti
                                                              #imagenes[0][:,0] me da las'x' de la imagen t=t0
                                                              #imagenes[0][:,1] me da las'y' de la imagen t=t0
ymin = min(imagenes[0][:,1])    #el min y max de la primera imagen sera max y min globales
ymax = max(imagenes[0][:,1])

plt.figure()
plt.xlim((xmin, xmax))
plt.ylim((ymin,ymax))
status = plt.ishold()
if status == True:
    plt.hold()   
for i in range(n):
    plt.plot(x=imagenes[i][:,0], y=imagenes[i][:,1])
    plt.show()