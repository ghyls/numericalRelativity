import numpy as np
#------------------------------------------------------------------

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










FIELD_ID = 0
x_resol = 50          #[1, inf]
time_resol = 50       #[1, inf]
cmap = 'magma'
grid = 1           #do you want a grid? 
grid_color = 'k'

#Set the following variable to "auto" if you want the title to be set 
#automatically. If not, you can know what you are plotting by looking at the 
#table displayed on the terminal.
plot_title = u"$\Phi(t, x)$ in a 2D simplified space-time (Mink)"
#plot_title = "auto"

text_scale = 0.9      #set it for fit the resolution of your screen
only_contours = False #Do you want the full plot colored or only the contours? 
#cmap can be, amongst others: plasma, bone, coolwarm, autumn, inferno
#------------------------------------------------------------------


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
#   z = all scalars (matrix (X·Y) with all scalrs for al timesteps)

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

print(x) 
timenew = time 
xnew = x
ZNEW = z
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#let's produce the plot

xnew, timenew = np.meshgrid(xnew, timenew)


addToTitle = '' #part of the title, taken from the first line of the file.
for word in lines[0]:
    addToTitle += word + ' '


#matplotlib stuff
import matplotlib.pyplot as plt

figure = plt.figure(figsize=(16,9.5))
ax1 = figure.add_subplot(111)

#generate labels for the contours
if only_contours:
    cont = ax1.contour(timenew,xnew,ZNEW, 20,cmap=cmap,rstride=1,cstride=1)
    figure.colorbar(cont, shrink=0.9) #the colorbar
else:   #TODO: add smoooth option
    cont = ax1.contourf(timenew,xnew,ZNEW, 20,cmap=cmap,rstride=1,cstride=1)
    cont = ax1.contourf(timenew,xnew,ZNEW, 20,cmap=cmap)

    figure.colorbar(cont, shrink=0.9) #the colorbar

    cont = ax1.contour(timenew,xnew,ZNEW, 20,\
         colors='w', linewidths=0.5, alpha=0.7, rstride=1,cstride=1)
    cont = ax1.contour(timenew,xnew,ZNEW, 20,\
         colors='w', linewidths=0.5, alpha=0.7)
         #linestyle='solid'


if grid: ax1.grid(linestyle='solid', axis='x', color=grid_color)


#labels and title
ax1.set_title (names[FIELD_ID] + u" vs $t$ in " +addToTitle , \
                                        fontsize = 24*text_scale, color = 'r')

ax1.set_ylabel ("spatial coordinate", fontsize = 16*text_scale)
ax1.set_xlabel ("temporal coordinate", fontsize = 16*text_scale)

if plot_title != "auto":
    ax1.set_title(plot_title, fontsize=18)

#set the number of ticks you want in each axis
plt.locator_params(axis='x', nbins=22)
plt.locator_params(axis='y', nbins=20)

#you can manually (by clicking), select where you want numerical labels
ax1.clabel(cont, inline = 1, manual=True, colors='w', fmt="%0.3f")

#Do you want to save the fig?
plt.savefig('a0.png', transparent=True)

#show the figure
plt.show()
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

