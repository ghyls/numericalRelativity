import numpy as np




dataFile = "Phi_2.x"

datos = np.loadtxt(dataFile)  #recordar tener cuidado con la ubicacion del 'Phi_2.x'

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

limits = [xmin, xmax, ymin, ymax] 


time = []
x = []
z = []

for i in range(len(imagenes)):

    time.append(i)
    z.append(imagenes[i][:,1])

x = imagenes[0][:,0]



#---------------------------------------------------------------------------
FIELD_ID = 2
transparency = 1    #[0, 1  ]
x_resol = 150          #[1, inf]
time_resol = 150       #[1, inf]
global_resolution = 1 #[1, inf]
elevation = 30        #[0, 90 ]
rotation = 320

#Set the following variables to "auto" if you want the title to be set 
#automatically. If not, you can know what you are plotting by looking at the 
#table displayed on the terminal.
plot_title = "$\Phi(t, x)$ in a 2D simplified space-time"
plot_zlabel = u"$\Phi(t, x)$"

text_scale = 0.7        #set it for fit the resolution of your screen
cmap = 'plasma'
#cmap can be, amongst others: plasma, bone, coolwarm, autumn, inferno
#---------------------------------------------------------------------------


f = open("tunnel_plot.txt", 'r')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#we take from the file "lines" ( list with splitted lines ) and names, 
#containing the scalar names.

lines = []

for line in f:
    line = list(line.split())
    lines.append(line)

names = [k for k in lines[3][2:]] 
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>    
# We print now the table with names and values corresponding with the 
# scalars

space = ' '
max_len = max([len(elem) for elem in names])

print("\n\n Available FIELD_ID's:\n") 
print("|    NAME  "+(max_len-13)*' '+"   |FIELD_ID |")  
print("|"+max_len*'-'+"+---------|")

for i, elem in enumerate(names):

    sp_units = max_len-len(elem)
    sp = space*sp_units
    print('|'+elem + sp + '     ' + str(i) + '    |')
print("\n\n")
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#We will now prepare the mesh. We need:
#
#   x = the spatial poossition (linspace(0, len(POINT_ID's)))
#   time: the "y" (list with all times)
#   z = all scalars (matrix (X x Y) with all scalrs for al timesteps)

'''

x = [float(elem) for elem in lines[1]]      #see the txt, 'x' is written in
                                            #the second line

timeSteps = []       #the timesteps, no the actual values of time.

for i in range(len(lines[2])):
    timeSteps.append(i)

time = [float(k) for k in lines[2]]         #the actual values of time



z = []          #2D array holding all the scalars
aux = []        #temporal array for constructing z   
time_index = 0  #we start on timestep 0 and go on
k = 4           #the line where scalar_values begins (see the txt)

while k < len(lines):

    line = lines[k]
    if float(line[0]) == timeSteps[time_index]:
    #if timestep has not changed
        aux.append(float(line[FIELD_ID+2]))
        #FIELD_ID+2 is the scalar selected. That's because before the 
        #scalars, we alredy have "time" and "point_ID".

        k += 1  #go to the next line

    else:  
        z.append(aux)   #append the whole timestep
        aux = []        #reset aux
        time_index += 1

z.append(aux)  #append the last timestep
'''
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#Let's interpolate the curve
'''
from scipy.interpolate import spline

z = np.array(z)

xnew = np.linspace(x[0], x[-1], x_resol) #the new array for x

timenew = np.linspace(time[0], time[-1], time_resol) #the new array for time

znew = []   #the new array for z

for timestep in z:
    aux = spline(x, timestep, xnew)
    znew.append(aux)

#we have interpolated the mesh in the 'x' axis. Let's do the same with the
#axis of time.

ZNEW = []
transposed = np.transpose(znew) #we transpose the array for match the 
                                #dimension of 'time' with the correct axis.
for pointstep in transposed:
    aux = spline(time, pointstep, timenew)
    ZNEW.append(aux)

ZNEW = np.transpose(ZNEW)   #go back to the original array
'''
timenew = time 
xnew = x
ZNEW = np.array(z)
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#let's produce the plot

xnew, timenew = np.meshgrid(xnew, timenew)


addToTitle = '' #part of the title, taken from the first line of the file.
for word in lines[0]:
    addToTitle += word + ' '


#we will use matplotlib's module "pyplot"
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.ticker as ticker

figure = plt.figure(figsize=(16,9.5))
ax1 = figure.add_subplot(111, projection='3d')

#generate the surface
surf = ax1.plot_surface(xnew, timenew, ZNEW, cmap=cmap, \
    alpha=transparency, antialiased=False ,rstride=global_resolution, \
    cstride=global_resolution)

#bg color and initial position of the camera
ax1.view_init(elevation, rotation)

#title and labels
ax1.set_title (names[FIELD_ID] + u" vs $t$ in " +addToTitle , \
                                        fontsize = 24*text_scale, color = 'r')
ax1.set_zlabel (names[FIELD_ID], fontsize = 16*text_scale, color = 'k')
ax1.set_xlabel (u"spatial space ($m$)", fontsize = 16*text_scale)
ax1.set_ylabel (u"temporal space ($s$)", fontsize = 16*text_scale)

if plot_title != "auto":
    ax1.set_title(plot_title, fontsize=16)
if plot_zlabel != "auto":
    ax1.set_zlabel (plot_zlabel, fontsize = 16)

#set limits of z axis, if necessary
#ax1.set_zlim(bottom = 0)

#function for formatting the colorbar in scientific notation
def fmt(x, pos):
    a, b = '{:.2e}'.format(x).split('e')
    b = int(b)
    return r'${} \times 10^{{{}}}$'.format(a, b)


#colorbar
figure.colorbar(surf, shrink=0.5, aspect=5, format=ticker.FuncFormatter(fmt))

#scientific notation
#plt.ticklabel_format(style='sci', axis='z', scilimits=(0,0))

#show the figure
plt.show()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<