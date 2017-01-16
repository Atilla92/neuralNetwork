import numpy as np 
import matplotlib.pyplot as plt
import sys


# Set stimulus parameters experiment
velStim = -0.25  #m/s velocity of stimulus
lStim = 0.01 #m  half length of stimulus
xStart = 0.05 #m start approach distance away from specimen 
fps = 200 # Frame Resolution
angPix = 4.5 # deg/pixel interommatidial angle specimen

#Name layers:
#nameFile = 'HueData' 
#nameFile = 'dataV025.dat' 
groupA1 = 'Hue'
groupB1 = ' Edge Detection '




#Imprt data from iqr neural network

def importData(nameFile):
	data= np.genfromtxt(nameFile, delimiter = ';')
	data= data[1:,:] #exclude first row nomenclature
	return data
#data = importData(nameFile)


# Read text file sampling data, extract ID
def findID(nameFile):
	IDNums=[]
	IDNames=[]
	IDMat = []

	with open(nameFile) as f:
		for line in f:
			line = line.strip()
			if '#' in line:
				printName = True
				IDFind=line.split('"')
				IDNumber = IDFind[2]
				IDNumber = IDNumber[1:]
				IDName=IDFind[1]

				if IDName in IDNames: 
				 	printName = False
				if printName == True: 
					IDNums.append(IDNumber)
					IDNames.append(IDName)
					lengthNum=int(len(IDNumber))
					IDMat.append ([IDNumber, IDName,lengthNum])
					IDName2 = IDName
		IDMat= np.asarray(IDMat)		
		IDMat =IDMat[np.sort(IDMat[:,2].argsort())[::-1]]
		IDNames = IDMat[:,1]
		IDNums = IDMat[:,0]
	return IDNums, IDNames


# Rewrite IDNumber with IDName
def rewriteCycleLine(nameFile):	
	IDNums, IDNames = findID(nameFile)
	with open(nameFile) as f:
		for line in f:
			line = line.strip()
			if 'cycle' in line:
				IDLine = line.split(';')
				for i in range(len(IDNames)):
					IDLine= [w.replace(str(IDNums[i]), IDNames[i]) for w in IDLine]
					IDLine= [w.replace('RangeAverage', 'RaAv') for w in IDLine]
	return IDLine
			
# Create custom defined plots
def createPlot(groupNameA, inhibitoryA, excitatoryA, cellPotentialA, activityA, averageA, neuronsA,nameFile):
	IDLine = rewriteCycleLine(nameFile)
	data = importData(nameFile)
	groupPlot = []
	partA = []
	partA2 = []
	time= data[:,0]
	if inhibitoryA == 1:
		partA.append('_inhIn_')
	if excitatoryA == 1 :
		partA.append('_excIn_')
	if cellPotentialA == 1:
		partA.append('_vm_')
	if activityA== 1:
		partA.append('_act_')
	if averageA == 1:
		partA2 = 'RaAv'
	showPlots = False

	for i in range(len(partA)):
		nameTrue=groupNameA + partA[i] + partA2
		if nameTrue in IDLine:
			columnGroup = data[:, IDLine.index(groupNameA + partA[i] + partA2)]
			groupPlot = plt.plot(time,columnGroup, label=groupNameA + partA[i] + partA2)
			plt.legend()
			showPlots = True
		else:
			print (nameTrue + ' is not in data list')
	if showPlots == True :
		plt.figure()
		plt.show(block = False)	
	return groupPlot, showPlots

#Make Plots, all data
def plotAllData(nameFile) :
	IDLine = rewriteCycleLine(nameFile)
	data = importData(nameFile)
	time= data[:,0] 
	for i in range(1, len(IDLine),1):
		allPlots= plt.plot(time, data[:,i], label =(str(IDLine[i])))
		plt.legend()
	return allPlots

# Make plot that only shows excitation

#def createTypePlot ():

# IDNums, IDNames = findID(nameFile)
# IDLine = rewriteCycleLine(nameFile,IDNames,IDNums)


partA = ['_act_', '_inhIn_']
partA2 = 'RaAv'
allGroups = False 
groupNames= [groupA1,groupB1]

def definePlots(nameFile, partA, partA2, allGroups, groupNames, scale,v):
	data = importData(nameFile)
	lOverV, v, l = extractValuesFileName(nameFile)
	IDLine = rewriteCycleLine(nameFile)
	time = data[:,0]* scale
	groupPlot = []

	IDLine2 = []
	if allGroups == True:
		groupNames= ['']

	for j in range(len(groupNames)):
		groupName = groupNames[j]
		#print groupName
		for i in range(1, len(IDLine),1):
			
			for k in range(len(partA)):
				nameTrue=groupName + partA[k] + partA2
				
				if nameTrue in IDLine[i]:
					ID = IDLine[i]
					print ID
					IDLine2.append(ID)
					columnGroup = data[:, i]
					groupPlot = plt.plot(time,columnGroup, label=(str(IDLine[i])+'_v_'+str(v)+'_l_'+str(l)+'_l/v_'+str(lOverV)))
					plt.legend()

	#plt.show()
	return groupPlot

# extract parameters Filename

#nameFile = 'data_v_0.25_l_0.01_type_square_pixDet_11_.dat'


def extractValuesFileName(nameFile):
	nameFileMat = nameFile.split('_')
	print nameFileMat
	if 'v' in nameFileMat: 
		v=nameFileMat[nameFileMat.index('v')+1]
	if 'l' in nameFileMat:
		l=nameFileMat[nameFileMat.index('l')+1]
	if 'pixDet' in nameFileMat:
		pixDet = nameFileMat[nameFileMat.index('pixDet')+1]
	if 'type' in nameFileMat:
		typeStim=nameFileMat[nameFileMat.index('type')+1]

	if 'v' and 'l' in nameFileMat:
		lOverV= np.divide(float(l),float(v))
	 	lOverV="{0:.2f}".format(lOverV)

	return  lOverV, v, l



#v, l, pixDet, typeStim, lOverV = extractValuesFileName(nameFile)

# allGroups = True
# plt.show()
# if allGroups == True:
# 	groupName = ''
# 	for i in range(1, len(IDLine),1):
# 		nameTrue=groupName + partA + partA2
		
# 		if nameTrue in IDLine[i]:
# 			ID = IDLine[i]
# 			IDLine2.append(ID)
# 			columnGroup = data[:, i]
# 			groupPlot = plt.plot(time,columnGroup, label=str(IDLine[i]))
# 			plt.legend()



	# for i in range(len(partA)):
	# 	if nameTrue in IDLine:
	# 		columnGroup = data[:, IDLine.index(partA[i] + partA2)]
	# 		groupPlot = plt.plot(time,columnGroup, label=str(IDLine[columnGroup]))
	# 		plt.legend()
	# 		showPlots = True
	# 	else:
	# 		print (nameTrue + ' is not in data list')
	# if showPlots == True :
	# 	plt.figure()
	# 	plt.show(block = False)	
	# return groupPlot, showPlots	


#create plots to compare
#name. inhibitory, excitatory, vm, act, average, neuron


# # IDNames = IDMat[:,1]
# # IDNums = IDMat[:,0]
# print IDNums



# IDMat= np.asarray(IDMat)


#Mat3 =IDMat2[np.argsort((IDMat2[:,2]))]
# IDMat =IDMat[IDMat[:,2].argsort()[::-1]]
# print IDMat
# # IDMat = []
# IDMat.append([])
# IDMa
# IDMat[0].append(IDNums)
# IDMat[1].append(IDNames)
# print IDMat 
# allPlots = plotAllData(IDLine, data)
# plt.show()
# groupPlotA= createPlot(' Edge Detection ', 1, 0,0, 0 ,1 ,0, data)
# groupPlotB= createPlot('Hue' , 0, 0,1, 0 ,1 ,0, data)
# plt.show()



# if foundA1 == True :
			# groupA1Exc_avg=data[1:-1, IDLine.index(groupA1 + '_excIn_RangeAverage')]
			# groupA1Vm_avg= data[1:-1, IDLine.index(groupA1 + '_vm_RangeAverage')]



# Calculate values stimulus
# from sys import path	
# path.append('/home/atilla/Documents/Test/Neural_Network/Stimulus/')
# from ommatidiaStimulus2 import getParamters
# tStim, lPixStim , thetaStim, xStim, dt = getParamters(velStim, xStart, fps, lStim, angPix)
# thetaNorm = (thetaStim - np.amin(thetaStim)) / (np.amax(thetaStim) - np.amin(thetaStim)) 
# #Scale time back to experiment
# #Not certain whether this scale is correct, i
# tStimScale = (tStim*len(data))+len(data)

# Define rows and columns of neural network data
#have to include to read file, so it does it automatically, search for the string Inh, etc and then take that column
# is in the firts row of the text file, so should be easy to implement
#also see what happens to data if more groups are added to the datasampling, how to classify



# g =open(nameFile, 'r')
# filedata = g.read()
# g.close()

# #for i in len(IDNums):
# newdata = filedata.replace(IDNums[1], IDNames[1])
# g=open('TextOut', 'w')
# g.write(newdata)
# g.close()

# if foundA1 == True:
# 	newdata = filedata.replace(IDGroupA1, groupA1)
# if foundB1 == True:
# 	g = open(nameFile, 'w')
# 	g.write(newdata)
# 	g.close()
#will probably produce an error if not there, 			
