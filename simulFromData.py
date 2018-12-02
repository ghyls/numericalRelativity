

from PyQt5 import QtCore, QtWidgets
import pyqtgraph as pg
from itertools import islice

import numpy as np 

from pyqtgraph import ScatterPlotItem










class MyWidget(pg.GraphicsWindow):
    
    ind = 0 
    dataFile = "temp.txt"
    def readTimeStep(self, index):
        with open(self.dataFile, "r") as f:
            line = next(islice(f, index, index+1))
        return line.split()
    
    def __init__(self, parent=None):
        
        self.lineLen = len(self.readTimeStep(0))
        
        super().__init__(parent=parent)

        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setLayout(self.mainLayout)

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1) # in milliseconds
        self.timer.start()
        self.timer.timeout.connect(self.onNewData)

        self.plotItem = self.addPlot(title="TheUniverse")


        self.plotItem.setXRange(-10, 10)
        self.plotItem.setYRange(-10, 10)

        self.plotDataItem = self.plotItem.plot([], pen=None, size=10,
            symbolBrush=(255,0,0), symbolSize=50, symbolPen=None)
        self.scatter = self.plotItem.plot(size=10, pen=None, symbolBrush=(255,0,0), symbolSize=5, symbolPen=None)  #brush=pg.mkBrush(255, 255, 255, 120

    def setData(self, x, y, allM):
        #self.plotDataItem.setData(x, y)
        size = [elem**0.3*3 for elem in allM]
        self.scatter.setData(x, y, symbolSize=size)

    def onNewData(self):

        try:
            line = self.readTimeStep(self.ind)
            allX = []
            allY = []
            allM = [float(line[1])]
            cont = 2
            while cont <= self.lineLen-2:
                try:
                    allX.append(float(line[cont]))
                    allY.append(float(line[cont+1]))
                    allM.append(float(line[cont+2]))
                    cont += 3
                except: break
            #print(allM)
            self.ind += 1
            self.setData(allX, allY, allM)
        except: self.timer.stop()


def main():
    
    app = QtWidgets.QApplication([])

    pg.setConfigOptions(antialias=False) # True seems to work as well

    win = MyWidget()
    win.show()
    win.resize(800,600) 
    win.raise_()
    app.exec_()
    
if __name__ == "__main__":
    main()