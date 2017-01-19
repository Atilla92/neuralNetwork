import numpy as np 
import matplotlib.pyplot as plt
import sys
from sys import path

path.append('/home/atilla/Documents/Test/Neural_Network/Stimulus/Add/')
import dataAnalysis as datAn

from dataAnalysis import findID, definePlots, extractValuesFileName, extractFiles, createPlotFiles, plotTimeCollision


# path.append('/home/atilla/Documents/Test/Neural_Network/Stimulus/Add/Data')

#filesIn =  os.listdir(path)

filePath= '/home/atilla/Documents/Test/Neural_Network/Stimulus/Add/'


#nameFiles = extractFiles(filePath)
#extractValuesFileName(nameFiles)




nameFile = 'data_v_0.25_l_0.01_type_square_pixDet_11_.dat'
nameFile2 = 'data_v_0.05_l_0.01_type_square_pixDet_11_.dat'
nameFile3 = 'data_v_0.4_l_0.01_type_square_pixDet_11_.dat'
nameFile4 = 'data_v_0.15_l_0.01_type_square_pixDet_11_.dat'
nameFile5 = 'data_v_0.18_l_0.01_type_square_pixDet_11_.dat'
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

groupNames= [groupA1, groupF1]#, groupE1]# groupC1, groupC2]
partA =['_act_']# ['_inhIn_']
partA2 = 'RaAv'
allGroups = False 
scale = 1



# plotTimeCol = False
# plotFile = False
# plotLGMDspike = False
# plotScatter = True
# setThresholdsMan = False
# setThresholdsSpikeMan = False

# thresholdHue = [0.001]
# thresholdSpike =[0.019 , 0.024, 0.028, 0.01 , 0.038, 0.01, 0.03 , 0.03]

# setColor = 'g'
# typeTrue = 'circle'
# plotDefineAgain, plotTimeCol, xTime2, plotSpikeCol, plotRegression1, xlv1, ysc1= datAn.createPlotFiles(filePath, partA, partA2, allGroups, groupNames, scale, plotFile, plotTimeCol, plotLGMDspike, plotScatter, setThresholdsMan, thresholdHue,  thresholdSpike, setThresholdsSpikeMan, typeTrue, setColor)


plotTimeCol = False
plotFile = False
plotLGMDspike = False
plotScatter = True
setThresholdsMan = False
setThresholdsSpikeMan = False
setColor = 'b'
thresholdHue = [0.1, 0.1,0.1, 0.2, 0.25 , 0.1, 0.25, 0.1]
thresholdSpike = 0.01
typeTrue = 'square'
plotDefineAgain, plotTimeCol, xTime2, plotSpikeCol, plotRegression2, xlv2, ysc2= datAn.createPlotFiles(filePath, partA, partA2, allGroups, groupNames, scale, plotFile, plotTimeCol, plotLGMDspike, plotScatter, setThresholdsMan, thresholdHue,  thresholdSpike, setThresholdsSpikeMan, typeTrue, setColor)


plotTimeCol = False
plotFile = False
plotLGMDspike = False
plotScatter = True
setThresholdsMan = False
setThresholdsSpikeMan = False
setColor = 'r'
#thresholdSpike =[0.019 , 0.024, 0.028, 0.01 , 0.038, 0.01, 0.03 , 0.03]
thresholdHue= [0.2, 0.2, 0.2, 0.1, 0.2,0.2, 0.4, 0.2, 0.2]
thresholdSpike = [0.04, 0.04 ,0.04, 0.1, 0.04, 0.04 , 0.04 , 0.04, 0.04]

typeTrue = 'Square(100)'
plotDefineAgain, plotTimeCol, xTime2, plotSpikeCol, plotRegression2, xlv3, ysc3= datAn.createPlotFiles(filePath, partA, partA2, allGroups, groupNames, scale, plotFile, plotTimeCol, plotLGMDspike, plotScatter, setThresholdsMan, thresholdHue,  thresholdSpike, setThresholdsSpikeMan, typeTrue, setColor)


# plotTimeCol = False
# plotFile = False
# plotLGMDspike = False
# plotScatter = True
# setThresholdsMan = False
# setThresholdsSpikeMan = False
# setColor = 'k'
# #thresholdSpike =[0.019 , 0.024, 0.028, 0.01 , 0.038, 0.01, 0.03 , 0.03]
# thresholdHue= [0.001]
# thresholdSpike = [0.01, 0.03, 0.015, 0.015, 0.015, 0.035, 0.01]

# typeTrue = 'Circle(100)'
# plotDefineAgain, plotTimeCol, xTime2, plotSpikeCol, plotRegression2, xlv3, ysc3= datAn.createPlotFiles(filePath, partA, partA2, allGroups, groupNames, scale, plotFile, plotTimeCol, plotLGMDspike, plotScatter, setThresholdsMan, thresholdHue,  thresholdSpike, setThresholdsSpikeMan, typeTrue, setColor)




plotTimeCol = False
plotFile = False
plotLGMDspike = False
plotScatter = True
setThresholdsMan = False
setThresholdsSpikeMan = False
setColor = 'k'
#thresholdSpike =[0.019 , 0.024, 0.028, 0.01 , 0.038, 0.01, 0.03 , 0.03]
thresholdHue= [0.4, 0.4, 0.4, 0.4, 0.4, 0.6 ,0.4, 0.4]
thresholdSpike = [0.02, 0.02, 0.01, 0.04,  0.003, 0.1, 0.03, 0.018]

typeTrue = 'TesCirc(100)'
plotDefineAgain, plotTimeCol, xTime2, plotSpikeCol, plotRegression2, xlv3, ysc3= datAn.createPlotFiles(filePath, partA, partA2, allGroups, groupNames, scale, plotFile, plotTimeCol, plotLGMDspike, plotScatter, setThresholdsMan, thresholdHue,  thresholdSpike, setThresholdsSpikeMan, typeTrue, setColor)

plt.show()
# plotLGMDspike = False
# plotTimeCol = False
# plotFile = False
# plotScatter = True
# setThresholdsMan = False
# typeTrue= 'circle'
# thresholdSpike = True
# plotDefineAgain, plotTimeCol, xTime2, plotSpikeCol, plotRegression,  xlv, ysc= datAn.createPlotFiles(filePath, partA, partA2, allGroups, groupNames, scale, plotFile, plotTimeCol, plotLGMDspike, plotScatter, setThresholdsMan, typeTrue, thresholdSpike, inputThresHue)


# plotLGMDspike = False
# plotTimeCol = False
# plotFile = False
# plotScatter = True
# setThresholdsMan = False
# typeTrue= 'square'
# thresholdSpike = True
# plotDefineAgain, plotTimeCol, xTime2, plotSpikeCol, plotRegression= datAn.createPlotFiles(filePath, partA, partA2, allGroups, groupNames, scale, plotFile, plotTimeCol, plotLGMDspike, plotScatter, setThresholdsMan, typeTrue, thresholdSpike)



#datAn.createPlotFiles(filePath, partA, partA2, allGroups, groupNames, scale)

#plt.show()
#plt.show()
# Congfigure own plots
groupNames= [groupA1, groupF1]#, groupE1]# groupC1, groupC2]
partA = ['_act_']#, '_inhIn_']
partA2 = 'RaAv'
typeTrue = ''
allGroups = False 
scale = 1






# import dataAnalysis3 as datAn
# #definePlots()
# plotDefine = datAn.definePlots(nameFile, partA, partA2, allGroups, groupNames, scale )
# #plt.show(block = False)
# scale =1
# plotDefine2 = datAn.definePlots(nameFile2, partA, partA2, allGroups, groupNames, scale )


# scale =1
# plotDefine2 = datAn.definePlots(nameFile3, partA, partA2, allGroups, groupNames,scale )


# scale =1
# plotDefine2 = datAn.definePlots(nameFile4, partA, partA2, allGroups, groupNames, scale )


# scale =1
# plotDefine2 = datAn.definePlots(nameFile5, partA, partA2, allGroups, groupNames, scale)

#plt.show()#block = False)








#First Data Set
#data = datAn.importData(nameFile)
#IDNums, IDNames = findID(nameFile)
#IDLineA = datAn.rewriteCycleLine(nameFile)
#Second Data Set 
#data2 = datAn.importData(nameFile2)
#IDNums2, IDNames2 = findID(nameFile2)
#IDLineA2 = datAn.rewriteCycleLine(nameFile2,IDNames2,IDNums2)

#Third Data Set 
#data3 = datAn.importData(nameFile3)
#IDNums3, IDNames3 = findID(nameFile3)
#IDLineA3 = datAn.rewriteCycleLine(nameFile3,IDNames3,IDNums3)



#create plots to compare
#name. inhibitory, excitatory, vm, act, average, neuron

# groupPlotA1, showPlots= datAn.createPlot(groupA1, 1, 1,1, 1 ,1 ,0, data, IDLine)
# groupPlotB1, showPlots= datAn.createPlot(groupB1, 1, 1,1, 1 ,1 ,0, data, IDLine)
# groupPlotC1, showPlots= datAn.createPlot(groupC1, 1, 1,1, 1 ,1 ,0, data, IDLine)
# groupPlotC2, showPlots= datAn.createPlot(groupC2, 1, 1,1, 1 ,1 ,0, data, IDLine)
# groupPlotD1= datAn.createPlot(groupD1, 1, 1,1, 1 ,1 ,0, data, IDLine)
# groupPlotD2= datAn.createPlot(groupD2, 1, 1,1, 1 ,1 ,0, data, IDLine)
# groupPlotD3= datAn.createPlot(groupD3, 1, 1,1, 1 ,1 ,0, data, IDLine)
# groupPlotD4= datAn.createPlot(groupD4, 1, 1,1, 1 ,1 ,0, data, IDLine)
# groupPlotE1= datAn.createPlot(groupE1, 1, 1,1, 1 ,1 ,0, data, IDLine)
# groupPlotE2= datAn.createPlot(groupE2, 1, 1,1, 1 ,1 ,0, data, IDLine)
# groupPlotF1= datAn.createPlot(groupF1, 1, 1,1, 1 ,1 ,0, data, IDLine)


# plt.figure()
# allPlots = datAn.plotAllData(IDLine, data)
# plt.show()

