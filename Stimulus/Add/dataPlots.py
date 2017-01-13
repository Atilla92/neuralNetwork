import numpy as np 
import matplotlib.pyplot as plt
import sys
from sys import path

path.append('/home/atilla/Documents/Test/Neural_Network/Stimulus/Add')
import dataAnalysis as datAn
from dataAnalysis import findID



nameFile = 'dataV025.dat' 
groupA1 = 'Hue'
groupB1 = ' Edge Detection '
groupC1 = 'ON cell' 
groupC2 = ' OFF cell'
groupD1 = 'EMD Up'
groupD2 = 'EMD Down'
groupD3 = 'EMD Left'
groupD4 = 'EMD Right' 
groupE1 = 'WTA Excit'
groupE2 = 'WTA Inhib'
groupF1 = 'LGMD WTA'


data = datAn.importData(nameFile)
IDNums, IDNames = datAn.findID(nameFile)
print IDNums
print IDNames
IDLine = datAn.rewriteCycleLine(nameFile,IDNames,IDNums)
print IDLine

plt.figure()
allPlots = datAn.plotAllData(IDLine, data)

plt.show()

#create plots to compare
#name. inhibitory, excitatory, vm, act, average, neuron
plt.figure()
groupPlotA1= datAn.createPlot(groupA1, 1, 1,1, 1 ,1 ,0, data, IDLine)
plt.show(block = False)
plt.figure()
groupPlotB1= datAn.createPlot(groupB1, 1, 1,1, 1 ,1 ,0, data, IDLine)
plt.show(block = False)
plt.figure()
groupPlotC1= datAn.createPlot(groupC1, 1, 1,1, 1 ,1 ,0, data, IDLine)
plt.show(block = False)
plt.figure()
groupPlotC2= datAn.createPlot(groupC2, 1, 1,1, 1 ,1 ,0, data, IDLine)
plt.show(block = False)

#plt.figure()
#groupPlotD1= datAn.createPlot(groupD1, 1, 1,1, 1 ,1 ,0, data, IDLine)
#plt.show(block = False)
# plt.figure()
# groupPlotD2= datAn.createPlot(groupD2, 1, 1,1, 1 ,1 ,0, data, IDLine)
# plt.show(block = False)
# plt.figure()
# groupPlotD3= datAn.createPlot(groupD3, 1, 1,1, 1 ,1 ,0, data, IDLine)
# plt.show(block = False)
plt.figure()
groupPlotD4= datAn.createPlot(groupD4, 1, 1,1, 1 ,1 ,0, data, IDLine)
plt.show(block = False)


plt.figure()
groupPlotE1= datAn.createPlot(groupE1, 1, 1,1, 1 ,1 ,0, data, IDLine)
plt.show(block = False)

plt.figure()
groupPlotE2= datAn.createPlot(groupE2, 1, 1,1, 1 ,1 ,0, data, IDLine)
plt.show(block = False)


plt.figure()
groupPlotF1= datAn.createPlot(groupF1, 1, 1,1, 1 ,1 ,0, data, IDLine)
plt.show()



