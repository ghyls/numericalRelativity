

from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
from itertools import islice

import numpy as np 

from pyqtgraph import ScatterPlotItem










class PlotGraphs(pg.GraphicsWindow):

    dataFile = "Psi_2.x"
    imagenes = []
    limits = []

    def readData(self):

        try:
            datos = np.loadtxt(self.dataFile)  #recordar tener cuidado con la ubicacion del 'Phi_2.x'
        except:
            datos = np.array([[0, 1], [0, 1]])
            print(self.dataFile + " not found")

        xmin = min(datos[:,0])
        xmax = max(datos[:,0])
        index = np.where(datos == xmax)[0]   #conozco el inicio (o el final) de cada bloque, me devuelve la posicion en datos[]
                                             #de cada elemento fin de bloque
        n = len(index)                       #la longitud de este array me dara el numero total de bloques (imagenes)
        self.imagenes = np.split(ary=datos, indices_or_sections=n, axis=0) #divido datos en cada uno de los bloques (imagenes)
                                                                    #axis=0 separa por filas (cada pareja de datos es una fila)
                                                                    #imagenes[i] me dara la imagen en t=ti
                                                                    #imagenes[0][:,0] me da las'x' de la imagen t=t0
                                                                    #imagenes[0][:,1] me da las'y' de la imagen t=t0
        ymin = min(self.imagenes[0][:,1])    #el min y max de la primera imagen sera max y min globales
        ymax = max(self.imagenes[0][:,1]) 

        self.limits = [xmin, xmax, ymin, ymax]


    ind = 0

    
    def __init__(self, parent=None):

        self.readData()

        xmin = self.limits[0]
        xmax = self.limits[1]
        ymin = self.limits[2]        
        ymax = self.limits[3]


        super().__init__(parent=parent)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(50) # in milliseconds
        self.timer.start()
        self.timer.timeout.connect(self.onNewData)

        self.plotItem = self.addPlot(title="Gravitational Wave 1 + 1 simulator")

        self.plotItem.setXRange(xmin, xmax)
        self.plotItem.setYRange(ymin, ymax)

        self.plotDataItem = self.plotItem.plot([], pen=pg.mkPen('c', width=3))
        #self.scatter = self.plotItem.plot(size=10, pen=None, symbolBrush=(255,0,0), symbolSize=5, symbolPen=None)  #brush=pg.mkBrush(255, 255, 255, 120

    def setData(self, x, y):
        self.plotDataItem.setData(x, y)
        #size = [elem**0.3*3 for elem in allM]
        #self.scatter.setData(x, y, symbolSize=size)

    def onNewData(self):

        try:    
            allX = self.imagenes[self.ind][:,0]
            allY = self.imagenes[self.ind][:,1]
            self.ind += 1
            self.setData(allX, allY)
        except Exception as e: 
            self.ind = 0
            print(e)
            #self.timer.stop()


def main():
    
    app = QtWidgets.QApplication([])

    pg.setConfigOptions(antialias=False) # True seems to work as well

    win = PlotGraphs()
    win.show()
    win.resize(800,600) 
    win.raise_()
    app.exec_()
    
if __name__ == "__main__":
    main()