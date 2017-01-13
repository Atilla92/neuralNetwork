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
nameFile = 'HueData' 
groupA1 = 'Hue'
groupB1 = 'Edge Detection'

#Imprt data from iqr neural network
data= np.genfromtxt(nameFile, delimiter = ';')
data= data[1:,:] #exclude first row nomenclature




# if 'Hue' in data1.read():
# 	print True


def findID(nameFile):
	IDNums=[]
	IDNames=[]
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
					IDName2 = IDName
	return IDNums, IDNames

def rewriteCycleLine(nameFile,IDNames,IDNums):	
	with open(nameFile) as f:
		for line in f:
			line = line.strip()
			if 'cycle' in line:
				IDLine = line.split(';')
				for i in range(len(IDNames)):
					IDLine= [w.replace(str(IDNums[i]), IDNames[i]) for w in IDLine]
					IDLine= [w.replace('RangeAverage', 'RaAv') for w in IDLine]
	return IDLine
			


			# print groupA1Exc_avg



# print IDFind
# print IDNums, IDNames



# foundA1 = False 
# foundB1 = False 


# with open(nameFile) as f:
# 	for line in f:
# 		line = line.strip()
# 		if groupA1 in line and foundA1 == False:
# 			IDlineA1 = line.split('=')
# 			IDGroupA1 = IDlineA1[1]
# 			#print IDGroupA1
# 			foundA1 = True
# 		if groupB1 in line and foundB1 == False:
# 			IDlineB1 = line.split('=')
# 			IDGroupB1 = IDlineB1[1]
# 			print IDGroupB1
# 			foundB1 = True
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





IDNums, IDNames = findID(nameFile)
IDLine = rewriteCycleLine(nameFile,IDNames,IDNums)
print IDLine

number = len(IDLine)

#Make Plots, all data  
time= data[:,0]
for i in range(1, len(IDLine),1):
	# ID = IDLine[i]
	# print ID
	plt.plot(time, data[:,i], label =(str(IDLine[i])))
	plt.legend()
	
plt.show()

print 


groupNameA= [ ' Edge Detection '] #Input group you want to plot

# allLinesA= False
inhibitoryA= 1
excitatoryA= 1
cellPotentialA= 0
activityA = 0
averageA = 1
neuronsA = 0


def createPlot(groupNameA, inhibitoryA, excitatoryA, cellPotentialA, activityA, averageA, neuronsA):
	partA = []
	partA2 = []
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


	for i in range(len(partA)):
		columnGroup = data[:, IDLine.index(groupNameA + partA[i] + partA2)]
		groupPlot = plt.plot(time,columnGroup, label=groupNameA + partA[i])
		plt.legend()

	return groupPlot


groupPlotA= createPlot(' Edge Detection ' , 0, 1,0, 0 ,1 ,0)
groupPlotB= createPlot('Hue' , 0, 0,1, 0 ,1 ,0)
plt.show()



# if foundA1 == True :
			# groupA1Exc_avg=data[1:-1, IDLine.index(groupA1 + '_excIn_RangeAverage')]
			# groupA1Vm_avg= data[1:-1, IDLine.index(groupA1 + '_vm_RangeAverage')]




# Calculate values stimulus
from sys import path	
path.append('/home/atilla/Documents/Test/Neural_Network/Stimulus/')
from ommatidiaStimulus2 import getParamters
tStim, lPixStim , thetaStim, xStim, dt = getParamters(velStim, xStart, fps, lStim, angPix)
thetaNorm = (thetaStim - np.amin(thetaStim)) / (np.amax(thetaStim) - np.amin(thetaStim)) 
#Scale time back to experiment
#Not certain whether this scale is correct, i
tStimScale = (tStim*len(data))+len(data)

# Define rows and columns of neural network data
#have to include to read file, so it does it automatically, search for the string Inh, etc and then take that column
# is in the firts row of the text file, so should be easy to implement
#also see what happens to data if more groups are added to the datasampling, how to classify



